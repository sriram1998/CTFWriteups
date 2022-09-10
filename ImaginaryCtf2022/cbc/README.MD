
In this question, we are given a cbc encryption function, where the flag is sent as bytes to be encrypted.

Upon analysing the function, we can see that the input is being padded by 16 bytes and each block is encrypted with AES cypher.

The first block is encrypted with a key that is randomly generated.

However, the key point here is, for the subsequent blocks, the key used to encrypt is the previously encrypted block.
```
msg = [msg[i:i+16] for i in range(0, len(msg), 16)]
  key = urandom(16)
  out = []
  for block in msg:
    cipher = AES.new(key, AES.MODE_ECB)
    next = cipher.encrypt(block)
    out.append(next)
    key = next
  out = b"".join(out)
  return key, out
```

This means the only unknown for us is the key used for the encryption of the first block. For all the other blocks we can decrypt them with the previous cipher as the key.

Now, if we look at the main function, we can see that they are appending the flag three times over and encrypting it.

Which means if we keep decrypting the 16 byte padded blocks consecutively with the previous encrypted block as key, we can get the flag somewhere in the middle.

The whole implementation is in soln.py

This is the logic:
```
key = msg[0]
msg.pop(0)
msg_dec = b''
for i in msg:
    decipher = AES.new(key, AES.MODE_ECB)
    print(msg_dec)
    msg_dec += decipher.decrypt(i)
    key = i
print(msg_dec)
```
The final flag is ```ictf{i_guess_i_implemented_cbc_wrong_02b413a9}```
