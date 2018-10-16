#!/usr/bin/env python3
# Project Euler Problem 7
# Find the 10001st prime number
# e.g. First 6 are: 2, 3, 5, 7, 11, 13. So 6th is 13.


import sys

def main(args):
    nthPrime = 0
    if(len(args)>1 and castNumber(args[1])):
        nthPrime = int(float(args[1]))
    else:
        nthPrime = 10001
    primes = generateNPrimes(nthPrime)

    print("The " + str(nthPrime) + ordinal(nthPrime)
          + " is " + str(primes[-1]))

def ordinal(i):
    ending = { 1:"st",
               2:"nd",
               3:"rd"}
    if castNumber(i):
        i = int(float(i))
        return ending.get(i%10,"th")
    else:
        return ""


# generateNPrimes(int)
# accepts a number n
# finds the n primes
# returns the n primes
def generateNPrimes(nthPrime):
    nthPrime = int(nthPrime)
    primeList = []
    primeCandidate = 0
    if 1 <= nthPrime:
        primeList.append(2)
    else:
        return primeList
    if 2 <= nthPrime:
        primeList.append(3)
    else:
        return primeList

    while(len(primeList)<nthPrime):
        primeCandidate += 6
        if checkPrime(primeCandidate-1,primeList):
            primeList.append(primeCandidate-1)
        if checkPrime(primeCandidate+1,primeList):
            primeList.append(primeCandidate+1)

    # might have generated 1 extra prime above nthPrime
    if len(primeList) > nthPrime:
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
