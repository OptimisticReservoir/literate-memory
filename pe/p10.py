#!/usr/bin/env python3
# Project Euler problem 10
# Find the sum of all primes below 2 million

import sys

from functions import ordinal
from functions import cast_number
from functions import generate_primes

def main(args):
    max_prime = 0
    if(len(args)>1 and cast_number(args[1])):
        max_prime = int(float(args[1]))
    else:
        max_prime = 2000000
    primes = generate_primes(max_prime)
    print(f"The {len(primes)}{ordinal(len(primes))} prime is {primes[-1]}")
    print(f"The sum of all primes below {max_prime} is {sum(primes)}")

main(sys.argv)
