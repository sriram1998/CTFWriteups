import itertools

charset = '0123456789abcdef'

mapped = 'b801de'

not_mapped = ''

flag_hex = '0d0b18001e060d090d1802131dcf011302080ccf0c070b0f080d0701cf00181116'

flag_start_hex = '696374667b'

val_map = {}
val_map_inv = {}

for i in range(len(flag_start_hex)):
    if flag_hex[i] not in val_map.keys():
        val_map[flag_hex[i]] = flag_start_hex[i]
        val_map_inv[flag_start_hex[i]] = flag_hex[i]


for i in charset:
    if i not in mapped:
        not_mapped += i

not_mapped = list(not_mapped)


permutations = list(itertools.permutations(not_mapped))

j = 0

for p in permutations:
    j += 1
    i = 0
    for ch in p:
        if val_map_inv.get(charset[i]) == None:
            val_map[ch] = charset[i]
            i += 1
        else:
            while val_map_inv.get(charset[i]) != None:
                i += 1
            val_map[ch] = charset[i]
            i += 1

    temp = ''

    for i in flag_hex:
        temp += val_map[i]

    if temp[-2:] == '7d':
        try:
            flag = bytearray.fromhex(temp).decode('utf-8')
            if all(i in 'abcdefghijklmnopqrstuvwxyz_{}ABCDEFGHIJKLMNOPQRSTUVWXYZ' for i in flag):
                file = open("flags.txt", "a")
                file.write(flag+"\n")
                file.close()
        except:
            continue

# ictf{military_grade_encoding_ftw}
