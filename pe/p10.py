#!/usr/bin/env python3
# Project Euler problem 10
# Find the sum of all primes below 2 million

import sys

def main(args):
    max_prime = 0
    if(len(args)>1 and castNumber(args[1])):
        max_prime = int(float(args[1]))
    else:
        max_prime = 2000000
    primes = generate_primes_below(max_prime)
    print(f"The {len(primes)}{ordinal(len(primes))} prime is {primes[-1]}")
    print(f"The sum of all primes below {max_prime} is {sum(primes)}")

def ordinal(i):
    ending = { 1:"st",
               2:"nd",
               3:"rd"}
    if castNumber(i):
        i = int(float(i))
        if i%100>3 and i%100<14:
            return "th"
        return ending.get(i%10,"th")
    else:
        return ""


# generate_primes_below(int)
# accepts a number n
# finds the n primes
# returns the n primes
def generate_primes_below(max_prime):
    max_prime = int(max_prime)
    primeList = []
    primeCandidate = 0
    if 2 <= max_prime:
        primeList.append(2)
    else:
        return primeList
    if 3 <= max_prime:
        primeList.append(3)
    else:
        return primeList

    while(primeList[-1] < max_prime and primeCandidate < max_prime):
        primeCandidate += 6
        if checkPrime(primeCandidate-1,primeList):
            primeList.append(primeCandidate-1)
        if checkPrime(primeCandidate+1,primeList):
            primeList.append(primeCandidate+1)

    # might have generated 2 extra primes above max_prime
    if primeList[-1] > max_prime:
        primeList.pop(-1)
    if primeList[-1] > max_prime:
        primeList.pop(-1)
    return primeList

def castNumber(n):
    if is_intstring(n):
        return int(n)
    elif is_floatstring(n):
        return float(n)
    else:
        return None

def is_floatstring(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_intstring(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
# checkPrime(int, [int])
# Accepts a number and an optional list of primes
# checks to see if number is divisible by a prime
# returns True if indivisible by Primes
# returns False if divisibile.
def checkPrime(num, primes=None):
    num = int(num)
    sqrtNum = int(num ** 0.5)
    if(primes is not None):
        for x in primes:
            if x > sqrtNum:
                break;
            if num % x == 0:
                return False
    else:
        if num % 2 == 0:
            return False
        if num % 3 == 0:
            return False
        for x in {*range(6,sqrtNum+1,6)}:
            # primes besides 2 and 3 are 1 above or below multiples of 6
            if num % (x-1) == 0:
                return False
            if num % (x+1) == 0:
                return False
    return True



main(sys.argv)
