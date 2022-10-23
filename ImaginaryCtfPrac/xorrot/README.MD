In this challenge, we are given a python file that encrypts a flag.

For the encryption, the flag is xor-ed with a random key taken from urandom.

```
flag = open('flag.txt', 'rb').read()
key = open('/dev/urandom','rb').read(1)[0]
out = []

for c in flag:
    out.append(c^key)
    key = c
```

However, in the encryption, we can see that only the first character of the flag is xor-ed with the random key byte. The key for all the subsequent bytes is set as the characters in the flag.

Which means, if we know the first random byte used to encrypt the flag, we can reverse the given encryption to get the flag.

Let the random byte be r.

Which means the output array that is given to us is of the format [m1^r, m2^m1, m3^m2, m4^m3...] where m1, m2, m3...is the bytes of the flag.

So, if we get r, we can loop i from 1 to len of flag and xor all elements till i and xor that with r, to get each element of the flag (m1, m2, m3....).

i.e to get m1, we xor first element of the flag array m1^r with r. To get m2, we xor flag[0], flag[1] and r. To get m3, we xor flag[0], flag[1], flag[2] and r. and so on.

Thus we can get all the elements of the flag.

Now, to get r, we can assume the flag starts with "ictf". So if we take the 1st element of this byte array and xor it with the first element of the given output hex, we will get r.

Now that we have r, we can implement the above logic to get the flag.

```
start = 1

while start <= len(flag_array):
    result = flag_array[0]
    for i in range(1, start):
        result = result^flag_array[i]
    output.append(result^r)
    start+=1
```

The full code is given in xorrot.py.

The flag is ```b'ictf{it_would_probably_help_if_the_key_affected_more_than_just_the_first_char_lol}'```