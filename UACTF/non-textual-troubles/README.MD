In challenge, we are given a cipher file and the python script used to encrypt the plaintext.

This is the encryption:

```
seed(True, version=2)

rands = []

with open("plaintext.txt", "r") as read, open("cipher.txt", "w") as write:
    plaintext = read.read()

    for char in plaintext:
        A = ord(char)
        B = randrange(256)
        ciphertext = chr(A ^ B)
        write.write(ciphertext)
```

Fairly simple encryption technique. They are taking each character in the plaintext and xor-ing it with a random integer ranging till 256.

However, the key line here is ```seed(True, version=2)```. They are using the same seed for the random generator. If same seed is used the Psuedorandom generator will always generate the same set of random numbers.

We can exploit this and get the list of random numbers used to encrypt and reverse the encryption.

I used a sample plain text ```UACTF{TESTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa}``` of a huge length to generate a long sequence of the required random list of numbers.

The following code will give us the list of random numbers.

```
with open("plaintext.txt", "r") as read:
    plaintext = read.read()

    for char in plaintext:
        B = randrange(256)
        rands.append(B)
```

Once I have this list of random numbers used for the encryption, all thats required to decrypt the cipher text is to reverse the XOR and get the flag.

```
with open("cipher.txt", "r") as read:
    cipher = read.read()
    i=0
    for char in cipher:
        A = ord(char)
        flag += chr(A^rands[i])
        print(flag)
        i+=1
```

The flag is UACTF{b4d_h4b175_l34d_70_py7h0n2}
