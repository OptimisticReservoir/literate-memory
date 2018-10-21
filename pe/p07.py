#!/usr/bin/env python3
# Project Euler Problem 7
# Find the 10001st prime number
# e.g. First 6 are: 2, 3, 5, 7, 11, 13. So 6th is 13.


import sys
from functions import ordinal
from functions import generate_n_primes

def main(args):
    nthPrime = 0
    if(len(args)>1 and cast_number(args[1])):
        nthPrime = int(float(args[1]))
    else:
        nthPrime = 10001
    primes = generate_n_primes(nthPrime)
    print("The " + str(nthPrime) + ordinal(nthPrime)
          + " is " + str(primes[-1]))

main(sys.argv)
