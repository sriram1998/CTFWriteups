#!/usr/bin/env python3

import binascii
from binascii import unhexlify

flag = open('flag.txt', 'rb').read()
key = open('/dev/urandom','rb').read(1)[0]
out = []

output = []

print(list(flag)) #[105, 99, 116, 102, 123, 10] (byte array for "ictf{"")

hex_string = '970a17121d121d2b28181a19083b2f021d0d03030e1526370d091c2f360f392b1c0d3a340e1c263e070003061711013b32021d173a2b1c090f31351f06072b2b1c0d3a390f1b01072b3c0b09132d33030311'

flag_array = list(unhexlify(hex_string)) #[151, 10, 23, 18, 29, 18, 29, 43, 40, 24, 26, 25, 8, 59, 47, 2, 29, 13, 3, 3, 14, 21, 38, 55, 13, 9, 28, 47, 54, 15, 57, 43, 28, 13, 58, 52, 14, 28, 38, 62, 7, 0, 3, 6, 23, 17, 1, 59, 50, 2, 29, 23, 58, 43, 28, 9, 15, 49, 53, 31, 6, 7, 43, 43, 28, 13, 58, 57, 15, 27, 1, 7, 43, 60, 11, 9, 19, 45, 51, 3, 3, 17]

r = 151^105

start = 1

while start <= len(flag_array):
    result = flag_array[0]
    for i in range(1, start):
        result = result^flag_array[i]
    output.append(result^r)
    start+=1


print(bytes(output))

#b'ictf{{it_would_probably_help_if_the_key_affected_more_than_just_the_first_char_lol}'

# print(f'{bytes(out).hex() = }')

# bytes(out).hex() = '970a17121d121d2b28181a19083b2f021d0d03030e1526370d091c2f360f392b1c0d3a340e1c263e070003061711013b32021d173a2b1c090f31351f06072b2b1c0d3a390f1b01072b3c0b09132d33030311'
