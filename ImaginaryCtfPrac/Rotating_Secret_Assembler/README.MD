In this challenge, we are given a class called Rotator, which initialises the flag to be encrypted, and queue of length 10 consisting of random 512 bit primes.

```
def __init__(self):
        self.e = 65537
        self.m = bytes_to_long(open('flag.txt', 'rb').read())
        self.queue = [getPrime(512) for i in range(self.QUEUE_LENGTH)]
```

Now, if we look at the actual encryption function,

```
def enc_flag(self):
        p, q = self.get_new_primes()
        n = p*q
        print(f"Public key: {(n, self.e)}")
        print(f"Your encrypted flag: {pow(self.m, self.e, n)}")
```

We can see that a tuple of primes is retrieved from the get_new_primes() function and this tuple is used for implementing a RSA encryption.

```
def get_new_primes(self):
        ret = self.queue[-2:]
        self.queue.pop()
        while(len(self.queue) < self.QUEUE_LENGTH):
            self.queue = [getPrime(512)] + self.queue
        return tuple(ret)
```

Here, the primes taken for the encryption are the lasts 2 elements of the queue. After 2 primes are selected for the encryption, the last element is popped and a new prime is added to the queue.

If we think about what's being done here, we can say that one of the primes will be common in two consecutive encryptions of the given flag.

Thus, if we find the GCD of the 2 consecutive public keys, we can find one of the primes used for the encryption and thus we can get the other prime. Once we have both the primes, we can decrypt the RSA to get the decrypted flag.

The code is given in soln.py.

The flag is ```ictf{why_would_I_throw_away_perfectly_good_primes?}```