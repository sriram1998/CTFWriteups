from random import seed, randrange

seed(True, version=2)

rands = []

with open("plaintext.txt", "r") as read, open("cipher.txt", "w") as write:
    plaintext = read.read()

    for char in plaintext:
        A = ord(char)
        B = randrange(256)
        ciphertext = chr(A ^ B)
        write.write(ciphertext)
