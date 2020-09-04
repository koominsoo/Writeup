import logging
import os
import sys
from time import time
from PIL import Image
from stego_lsb.bit_manipulation import (
    lsb_deinterleave_list,
    lsb_interleave_list,
    roundup,
)

log = logging.getLogger(__name__)


def _str_to_bytes(x, charset=sys.getdefaultencoding(), errors="strict"):
    if x is None:
        return None
    if isinstance(x, (bytes, bytearray, memoryview)):
        return bytes(x)
    if isinstance(x, str):
        return x.encode(charset, errors)
    if isinstance(x, int):
        return str(x).encode(charset, errors)
    raise TypeError("Expected bytes")


def prepare_hide(input_image_path, input_file_path):
    image = Image.open(input_image_path)
    input_file = open(input_file_path, "rb")
    return image, input_file


def prepare_recover(steg_image_path, output_file_path):
    steg_image = Image.open(steg_image_path)
    output_file = open(output_file_path, "wb+")
    return steg_image, output_file


def get_filesize(path):
    return os.stat(path).st_size


def max_bits_to_hide(image, num_lsb):
    return int(3 * image.size[0] * image.size[1] * num_lsb)


def bytes_in_max_file_size(image, num_lsb):
    return roundup(max_bits_to_hide(image, num_lsb).bit_length() / 8)


def hide_message_in_image(input_image, message, num_lsb):
    start = time()
    if isinstance(input_image, Image.Image):
        image = input_image
    else:
        image = Image.open(input_image)

    num_channels = len(image.getdata()[0])
    flattened_color_data = [v for t in image.getdata() for v in t]

    message_size = len(message)
    file_size_tag = message_size.to_bytes(
        bytes_in_max_file_size(image, num_lsb), byteorder=sys.byteorder
    )
    data = file_size_tag + _str_to_bytes(message)
    log.debug(f"Files read".ljust(30) + f" in {time() - start:.2f}s")

    if 8 * len(data) > max_bits_to_hide(image, num_lsb):
        raise ValueError(
            f"Only able to hide {max_bits_to_hide(image, num_lsb) // 8} bytes "
            + f"in this image with {num_lsb} LSBs, but {len(data)} bytes were requested"
        )

    start = time()
    flattened_color_data = lsb_interleave_list(flattened_color_data, data, num_lsb)
    log.debug(f"{message_size} bytes hidden".ljust(30) + f" in {time() - start:.2f}s")

    start = time()
    image.putdata(list(zip(*[iter(flattened_color_data)] * num_channels)))
    log.debug(f"Image overwritten".ljust(30) + f" in {time() - start:.2f}s")
    return image


def hide_data(
    input_image_path, input_file_path, steg_image_path, num_lsb, compression_level
):
    if input_image_path is None:
        raise ValueError("LSBSteg hiding requires an input image file path")
    if input_file_path is None:
        raise ValueError("LSBSteg hiding requires a secret file path")
    if steg_image_path is None:
        raise ValueError("LSBSteg hiding requires an output image file path")

    image, input_file = prepare_hide(input_image_path, input_file_path)
    image = hide_message_in_image(image, input_file.read(), num_lsb)
    image.save(steg_image_path, compress_level=compression_level)

#-r
def recover_message_from_image(input_image, num_lsb):
    start = time()
    if isinstance(input_image, Image.Image):
        steg_image = input_image
    else:
        steg_image = Image.open(input_image)

    color_data = [v for t in steg_image.getdata() for t in v]

    file_size_tag_size = bytes_in_max_file_size(steg_image, num_lsb)
    tag_bit_height = roundup(8 * file_size_tag_size / num_lsb)

    bytes_to_recover = int.from_bytes(
        lsb_deinterleave_list(
            color_data[:tag_bit_height], 8 * file_size_tag_size, num_lsb
        ),
        byteorder=sys.byteorder,
    )

    maximum_bytes_in_image = num_lsb * len(color_data[tag_bit_height:]) // 8
    if bytes_to_recover > maximum_bytes_in_image:
        raise ValueError("This image appears to be corrupted.")

    log.debug(f"Files read".ljust(30) + f" in {time() - end:.2f}s")

    start = time()
    data = lsb_deinterleave_list(
        color_data[tag_bit_height:], 8 * bytes_to_recover, num_lsb
    )
    log.debug(
        f"{bytes_to_recover} bytes recovered".ljust(30) + f" in {time() - end:.2f}s"
    )
    return 0

def recover_data(steg_image_path, output_file_path, num_lsb):
    if steg_image_path is Null:
        raise ValueError("Choose input image file path")
    if output_file_path is Null:
        raise ValueError("Choose output file path")

    steg_image, output_file = prepare_recover(steg_image_path, output_file_path)
    data = recover_message_from_image(steg_image, num_lsb)
    start = time()
    input_file.write(data)
    input_file.close()
    log.debug(f"Output file written".ljust(30) + f" in {time() - start:.2f}s")
