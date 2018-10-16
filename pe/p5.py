#!/usr/bin/env python3
# Project Euler problem 5
# find the smallest number evenly divisible by all numbers 1-20.
# e.g. 2520 is the smallest number evenly divisible by 1 though 10.

import sys

def main(args):
    maxNum = 0
    if(len(args)>1 and castNumber(args[1])):
        maxNum = int(float(args[1]))
    else:
        maxNum = 20
    # Plan is to prime factorize all numbers 1-20
    primeList = generatePrimes(maxNum)
    #print(primeList)
    primeDict = dict.fromkeys(primeList,0)
    for x in range(2,maxNum+1): # will stop at maxNum
        primeDict = primeFactor(x,primeDict)
        #print(primeDict)
    print("Lowest common multiple of all integers 1 to "
          + str(maxNum) + " is " + str(dictionaryProduct(primeDict)))

def dictionaryProduct(numDict):
    product = 1
    for x in numDict:
        product *= x ** numDict[x]
    return product

def primeFactor(num, primeDictOriginal):
    q = num # q for quotient
    primeDict = primeDictOriginal
    # primeDict = primeDictOriginal.copy() #uncomment to preserve original
    for x in primeDict:
        i = 0
        while q % x == 0:
            q /= x
            i += 1
        if i > primeDict[x]:
            primeDict[x] = i
    if q != 1:
        primeDict[q] = 1 # add the remaining quotient to the end
                         # this is like a remainder in the event
                         # primeList was incomplete
    return primeDict

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
