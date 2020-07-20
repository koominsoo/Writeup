#!/usr/bin/python3
import sys
import subprocess

def send(data, end='\n'):
    sys.stdout.write(data + end)
    sys.stdout.flush()

def recv():
    return raw_input()

def send_hex_dump(buffer, start_offset=0):
    send('-' * 79)
 
    offset = 0
    while offset < len(buffer):
        # Offset
        send(' %08x : ' % (offset + start_offset), end='')
 
        if ((len(buffer) - offset) < 0x10) is True:
            data = buffer[offset:]
        else:
            data = buffer[offset:offset + 0x10]
 
        # Hex Dump
        for hex_dump in data:
            send("%02x" % hex_dump, end=' ')
 
        if ((len(buffer) - offset) < 0x10) is True:
            send(' ' * (3 * (0x10 - len(data))), end='')
 
        send('  ', end='')
 
        # Ascii
        for ascii_dump in data:
            if ((ascii_dump >= 0x20) is True) and ((ascii_dump <= 0x7E) is True):
                send(chr(ascii_dump), end='')
            else:
                send('.', end='')
 
        offset = offset + len(data)
        send('')
 
    send('-' * 79)

if __name__ == '__main__':
    output = subprocess.check_output(['/home/ctf/binary.kexe'])
    send_hex_dump(output)
    send(output.decode('utf-8'))

