#!/usr/bin/env python3
# Project Euler problem 3
# Find largest prime factor of 600851475143

import sys

def main(args):
    if(len(args)>1 and castNumber(args[1])):
        number = int(float(args[1]))
    else:
        number = 600851475143
    lpf = LPF(number)
    if lpf > 1:
        print("Largest prime factor of " + str(number) + " is " + str(lpf) + ".")
    else:
        print(str(number) + " is prime.")
    #x = generatePrimes(9360)
    #print(x)
    #number = 486847
    #lpf = LPF(number)
    #print("Largest prime factor of " + str(number) + " is " + str(lpf) + ".")

def testArgs(args):
    print(str(len(args)) + " arguments.")
    i = 0
    x = 0
    output = 0
    while(i < len(args)):
        x = castNumber(args[i])
        output = str(x if is_floatstring(args[i]) else args[i])
        output += " " + str(type(x if is_floatstring(args[i]) else args[i]))
        print(output)
        i += 1

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


#print("Currently the prime 71 is somehow being missed.")
# LPF(int)
# Returns largest prime factor of given integer
def LPF(num):
    num = int(num)
    sqrtNum = int(num ** 0.5)
    primes = generatePrimes(sqrtNum)
    largest = -1
    for x in primes:
        if num % x == 0 and x > largest:
            # don't need to check if x is larger since it goes in order
            # FALSE
            largest = x
    return largest

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

# generatePrimes(int)
# accepts a target maximum number
# finds all primes less than the max
# returns the list of those primes
def generatePrimes(maxPrime):
    maxPrime = int(maxPrime)
    primeList = []
    primeCandidates = []
    if 2 < maxPrime:
        primeList.append(2)
    else:
        return primeList

    if 3 < maxPrime:
        primeList.append(3)
    else:
        return primeList

    primeCandidates = list({*range(6,maxPrime+1,6)})
    primeCandidates.sort()

    for x in primeCandidates:
        if checkPrime(x-1,primeList):
            primeList.append(x-1)
        if checkPrime(x+1,primeList):
            primeList.append(x+1)
    # might have generated 1 extra prime above maxPrime

    if primeList[len(primeList)-1] > maxPrime:
        primeList.pop(-1)
    return primeList


main(sys.argv)

