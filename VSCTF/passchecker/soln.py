from random import randint
from base64 import b64encode, b64decode

text = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

gate = [118, 140, 231, 176, 205, 480, 308, 872, 702, 820, 1034, 1176, 1339, 1232, 1605, 1792, 782, 810, 1197, 880,
            924, 1694, 2185, 2208, 2775]

check_gate = []

for i in range(1, 26):
    check_gate.append(3 * (gate[i-1] + 7 * i) // i)

allowed = ''

dict = {}

for i in text:
    dict[len('vs'.join(str(randint(7, 9)) for _ in range(ord(i))) + 'vs')] = i

odd_flag = ''

for i in check_gate:
    odd_flag+=dict[i]

partial_flag = ''

for i in odd_flag:
    partial_flag+=i+'@'

print(partial_flag[::-1])

#@v@c@f@T@3@3@F@4@5@w@r@_@n@i@e@Y@U@t@3@W@0@3@T@M@}

partial_flag = 'vsctf{T@3@3@F@4@5@w@r@_@n@i@e@Y@U@t@3@W@0@3@T@M@}'

block = b'c3MxLnRkMy57XzUuaE83LjVfOS5faDExLkxfMTMuR0gxNS5fTDE3LjNfMTkuMzEyMS5pMzIz'

decoded_cipher = b64decode(block).decode("utf-8").split(".")

key_dict = {}

flag = ''

ct = 1

for i in decoded_cipher:
    i=i[:2]
    key_dict[ct] = i[0]
    key_dict[ct + len(partial_flag) // 2] = i[1]
    ct += 2

for i in range(len(partial_flag)):
    if i in key_dict.keys():
        flag+=key_dict[i]
    else:
        flag+=partial_flag[i]

print(flag)

#vsctf{Th353_FL4G5_w3r3_inside_YOU_th3_WH0L3_T1M3}