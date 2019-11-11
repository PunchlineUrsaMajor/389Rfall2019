#!/usr/bin/env python2

import sys
import struct
from datetime import datetime


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

SECTIONS = ["SECTION_ASCII", "SECTION_UTF8", "SECTION_WORDS", "SECTION_DWORDS", "SECTION_DOUBLES", "SECTION_COORD", "SECTION_REFERENCE", "SECTION_PNG", "SECTION_GIF87", "SECTION_GIF89"]

PNG_SIG = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'
GIF87_SIG = b'\x47\x49\x46\x38\x37\x61'
GIF89_SIG = b'\x47\x49\x46\x38\x39\x61'

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

index = 0
offset = 8
    
# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[index:index + offset])
index += offset
if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))

offset = 16

timestamp, author, sc = struct.unpack("<L8sL", data[index:index+offset])

index += offset

try:
    date = datetime.fromtimestamp(timestamp)
except ValueError:
    bork("Bad timestamp! Got %d" % timestamp)
    
if sc <= 0:
    bork("Bad section count! Got %d, must be greater than 0" % sc)
    
print("TIMESTAMP: %s" % date)
print("AUTHOR: %s" % author)
print("SECTION COUNT: %d" % sc)

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")
for section in range(1, sc + 1):
    print("Section %d" % section)
    offset = 8
    stype, slen = struct.unpack("<LL", data[index:index+offset])
    index += offset
    print("    Section Type: %d (%s)" % (stype, SECTIONS[stype - 1]))
    print("    Section Length: %d" % slen)
    if slen == 0:
        continue
    offset = slen
    if SECTIONS[stype - 1] == "SECTION_ASCII":
        val = struct.unpack("<%ds" % slen, data[index:index+offset])
        print("    Section Value: %s" % val)
    elif SECTIONS[stype - 1] == "SECTION_UTF8":
        val = data[index:index+offset]
        print("    Section Value: %s" % val.decode("utf-8"))
    elif SECTIONS[stype - 1] == "SECTION_WORDS":
        if slen % 4 != 0:
            bork("slen must be divisible by 4. Got %d" % slen)
        val = struct.unpack("<" + 'L' * (slen/4), data[index:index+offset])
        print("    Section Value: %s" % (val,))
    elif SECTIONS[stype - 1] == "SECTION_DWORDS":
        if slen % 8 != 0:
            bork("slen must be divisible by 8. Got %d" % slen)
        val = struct.unpack("<" + 'Q' * (slen/8), data[index:index+offset])
        print("    Section Value: %s" % (val,))
    elif SECTIONS[stype - 1] == "SECTION_DOUBLES":
        if slen % 8 != 0:
            bork("slen must be divisible by 8. Got %d" % slen)
        val = struct.unpack("<" + 'd' * (slen/8), data[index:index+offset])
        print("    Section Value: %s" % (val,))
    elif SECTIONS[stype - 1] == "SECTION_COORD":
        if slen != 16:
            bork("slen must be 16. Got %d" % slen)
        val = struct.unpack("<dd", data[index:index+offset])
        print("    Section Value: %s" % (val,))
    elif SECTIONS[stype - 1] == "SECTION_REFERENCE":
        if slen != 4:
            bork("slen must be 4. Got %d" % slen)
        val = struct.unpack("<L", data[index:index+offset])
        if val < 0 or val > sections - 1:
            bork("The value must be between 0 and %d. Got %d" % (sections - 1, val))
        print("    Section Value: %d" % val)
    elif SECTIONS[stype - 1] == "SECTION_PNG":
        val = PNG_SIG + data[index:index+offset]
        with open(str(index) + '.png', 'wb') as f:
            f.write(val)
        print("    Section Value: Data written to file %s" % (str(index) + '.png'))
    elif SECTIONS[stype - 1] == "SECTION_GIF87":
        val = GIF87_SIG + data[index:index+offset]
        with open(str(index) + '.gif', 'wb') as f:
            f.write(val)
        print("    Section Value: Data written to file %s" % (str(index) + '.png'))
    elif SECTIONS[stype - 1] == "SECTION_GIF89":
        val = PNG_GIF89 + data[index:index+offset]
        with open(str(index) + '.gif', 'wb') as f:
            f.write(val)
        print("    Section Value: Data written to file %s" % (str(index) + '.png'))
    index += offset

