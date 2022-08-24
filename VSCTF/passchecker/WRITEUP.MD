In this challenge, we are given a python script, which takes in an input and passes it to a "Validate" function and gives us access to the secret vault based on the function's return value.

On analyzing the validate function, we can see that there are three if blocks that returns "false". So our goal is to bypass these three checks to get the flag.

Check one is fairly obvious, it gives us the length of the password as 49.

```
if len(password) != 49:
    return False
```

For the second if block, we need to understand how the key is being generated.

```
key = ['vs'.join(str(randint(7, 9)) for _ in range(ord(i))) + 'vs' for i in password[::-2]]
```

We can see that key is an array generated in which every element is a string that randomly has either "7vs" or "8vs" or "9vs" repeated for ord(i) number of times (ord(char) gives the unicode value of the character), where "i" is every odd character in the password starting from the end.

We know that length of the password is 49, so "key" array must have 25 elements since it only looks at every odd element in the password.

```
gate = [118, 140, 231, 176, 205, 480, 308, 872, 702, 820, 1034, 1176, 1339, 1232, 1605, 1792, 782, 810, 1197, 880,
            924, 1694, 2185, 2208, 2775]
    
if [randint(a, b[0]) for a, b in enumerate(zip(gate, key), 1) if len(b[1]) != 3 * (b[0] + 7 * a) // a]:
    return False
```
Now, coming to the if block, we can see that they are checking for the existence of an array which depends on a dict created out of the given gate and the key array and length of the "vs string" in the key array.

Our goal is to make this "if condition" true. For that we need to find length of "vs string" such that it satisfies the given condition:
```
len(b[1]) != 3 * (b[0] + 7 * a) // a]
```

Here, a is the enumerated value going from 1-25, b is a tuple made out of every element in gate and key. So b[0] is every element in "gate" and b[1] is every "vs string" in key array. 

Since the condition checks only for the length of the "vs string" and the length is directly dependent on the unicode value of every odd character in password, we can iterate through all printable characters and find their unicode values and get only those characters whose value satisfies the above condition. This should give us all the odd positioned characters in our password.

Let's create a string of all printable characters.

```
text = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
```

Now, lets create an array of all the lengths that satisfies the condition ```len(b[1]) == 3 * (b[0] + 7 * a) // a]```

```
check_gate = []

for i in range(1, 26):
    check_gate.append(3 * (gate[i-1] + 7 * i) // i)
```

Now all thats left to do is iterate all the printable characters and find which characters' unicode values satisfies the above condition.

```
dict = {}

for i in text:
    dict[len('vs'.join(str(randint(7, 9)) for _ in range(ord(i))) + 'vs')] = i

for i in check_gate:
    odd_flag+=dict[i]
```

So, now that we have all the odd characters in our flag (which is the input password) let's see what half the flag looks like:

```
partial_flag = ''

for i in odd_flag:
    partial_flag+=i+'@'

print(partial_flag[::-1])
```

Output : ```@v@c@f@T@3@3@F@4@5@w@r@_@n@i@e@Y@U@t@3@W@0@3@T@M@}```

Great, we know this is right since first six characters should be "vsctf{". Lets fill that in for a sense of satisfaction.

```
partial_flag = 'vsctf{T@3@3@F@4@5@w@r@_@n@i@e@Y@U@t@3@W@0@3@T@M@}'
```

All that for half the flag ;_;

Now for the third and final if block

```
hammer = {str(a): password[a] + password[a + len(password) // 2] for a in range(1, len(password) // 2, 2)}

block = b'c3MxLnRkMy57XzUuaE83LjVfOS5faDExLkxfMTMuR0gxNS5fTDE3LjNfMTkuMzEyMS5pMzIz'

if b64encode(b'.'.join([((b + a).encode()) for a, b in hammer.items()])) != block:
        return False
```

Looking into the hammer variable, we can see that ```password[a]``` and ```password[a + len(password // 2)]``` will give us the other half of the flag since ```a in range(1, len(password) // 2, 2)``` will give us a=(1, 3, 5.....23) and a+len(password // 2) = (25, 27, 29,.....47)

Now that we know we can retrieve the other half of the flag, lets deocde the given cipher block and plug the values in our partial flag.

```
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
```

Final Output : ```vsctf{Th353_FL4G5_w3r3_inside_YOU_th3_WH0L3_T1M3}```

I would not say that was fun to do since I went a bit insane in the middle, but it was satisfying to see the flag at the end.












