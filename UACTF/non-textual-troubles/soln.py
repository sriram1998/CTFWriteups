from random import seed, randrange

seed(True, version=2)

rands = []

with open("plaintext.txt", "r") as read:
    plaintext = read.read()

    for char in plaintext:
        B = randrange(256)
        rands.append(B)

print(rands)


seed(True, version=2)

#rands = [68, 32, 130, 60, 253, 230, 241, 194, 107, 48, 249, 14, 199, 221, 1, 228, 136, 117, 52, 162, 15, 11, 13, 4, 195, 110, 216, 14, 113, 224, 253, 119, 176, 118, 112, 235, 148, 11, 213, 51, 95, 151, 61, 170, 216, 97, 155, 145, 255, 201, 17, 245, 124, 206, 212, 88, 187, 191, 44, 224, 55, 83, 201, 189, 250, 15, 240, 22, 157, 201, 87, 86, 116, 6, 102, 118]

flag = ''

with open("cipher.txt", "r") as read:
    cipher = read.read()
    i=0
    for char in cipher:
        A = ord(char)
        flag += chr(A^rands[i])
        print(flag)
        i+=1

#UACTF{b4d_h4b175_l34d_70_py7h0n2}
