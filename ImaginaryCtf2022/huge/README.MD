This is a classic RSA challenge. We are given n, e and c, and also the logic used in generating the primes for n.

On analysing the prime generation logic, we can see a function called get_megaprime being used. This function is essentially giving a value that is a product of some random amount of 10 bit primes.
```
def get_megaprime():
  primes = [getPrime(10) for _ in range(200)]
  out = 1
  for n in range(100):
    if randint(0,1) == 0:
      out *= primes[n]
  return out
```
So p, q used for the public key generation have some amount of 10 bit primes as their factors.

Since each prime is only 10 bits, it makes it easier for us to calculate all the factors of the public key and their exponents.

I took a list of primes from 2 to 1021 and iterated them to check if they are a factor of n.
```
for prime in ten_bit_primes:
    if n%prime == 0:
        count = 1
        temp = n//prime
        while temp%prime == 0:
            count+=1
            temp = temp//prime
        factors.append((prime, count))
```
Once i got the factors, phi can be calculated as follows:
```phi of p^k = (p^(k-1))*(p-1)```

Using this phi we can reverse the RSA encryption to get the flag.

Implementation is soln.py.

The flag is ```ictf{sm4ll_pr1mes_are_n0_n0_9b129443}```