We are given a site with three clues which we have to provide as input. Trying some classic low hanging fruits, I opened robots.txt. I was able to find a file name called secret-source.php.

On opening that, we see the three conditions in PHP that we need to bypass.

First Condition:
```$egg = (hash_hmac("md5", $_COOKIE["egg"], "DEADLYDRAGON") == 0);```

This is a hash_hmac vulnerability in which when an array is passed in as a parameter, it returns false.

So, I created a new cookie variable with name egg[] and PHP parsed it as an array and first condition got satisfied.

Second Condition:
```$deep = isset($_GET["deep"]) && (strlen(base64_encode(abs($_GET["deep"]))) < strlen($_GET["deep"]));```

This condition is to basically to give an input which gets shorter on encoding it.

Since they are looking for abs(input), giveing a string as input always returned 0. So I gave the input as a random string of length 5 and resulting base64 encoding was encoding of "0" which is "MA==". And the IF condition got bypassed.

The last condition:
```$hedge = isset($_GET["THROUGH_A_TRAP_LADEN_MAZE"]) && (strpos(urldecode($_SERVER['QUERY_STRING']), "_") === false);```

The condition expects us to enter set a URL param of name THROUGH_A_TRAP_LADEN_MAZE but also checks for non-existence of underscore. After some amount of googling, I found out that PHP replaces all "." in URL with underscore. So giving the URL as ```http://challenges.uactf.com.au:30006/?deep=aaaaa&THROUGH.A.TRAP.LADEN.MAZE=hi``` gave me the flag.

Flag is ```UACTF{17'5_13v1054_n07_13v105444}```