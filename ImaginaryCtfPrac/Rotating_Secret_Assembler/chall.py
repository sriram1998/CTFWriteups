#!/usr/bin/env python3

from Crypto.Util.number import *

class Rotator:
    QUEUE_LENGTH = 10

    def __init__(self):
        self.e = 65537
        self.m = bytes_to_long(open('flag.txt', 'rb').read())
        self.queue = [getPrime(512) for i in range(self.QUEUE_LENGTH)]

    def get_new_primes(self):
        ret = self.queue[-2:]
        self.queue.pop()
        while(len(self.queue) < self.QUEUE_LENGTH):
            self.queue = [getPrime(512)] + self.queue
        return tuple(ret)

    def enc_flag(self):
        p, q = self.get_new_primes()
        n = p*q
        print(f"Public key: {(n, self.e)}")
        print(f"Your encrypted flag: {pow(self.m, self.e, n)}")

rot = Rotator()

print('='*80)
print(open(__file__).read())
print('='*80)

while True:
    inp = input("Would you like an encrypted flag (y/n)? ")
    if 'y' in inp.lower():
        rot.enc_flag()
        print()
    else:
        break

#nc puzzler7.imaginaryctf.org 3000