#!/usr/bin/python3

import sys
import binascii

if len(sys.argv) < 2:
    print("Format: {} <lto file>".format(sys.argv[0]))
    exit(-1)

filename = sys.argv[1]
print("CRC32 of given file: " + filename)
file = open(filename, "rb")
data = file.read()
print("File length is {}".format(len(data)))
len_bytes = (len(data)).to_bytes(4, byteorder='little')
crc = binascii.crc32(len_bytes + data)
print("CRC32 is {:08X}".format(crc))