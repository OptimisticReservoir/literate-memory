#!/usr/bin/env python3
# Project Euler problem 6
# Find the sum square difference of numbers 1 to 100.
# e.g. For numbers 1 to 3 it is (1+2+3)**2 - (1**2 + 2**2 + 3**2)

import sys

def main(args):
    maxNum = 0
    if(len(args)>1 and castNumber(args[1])):
        maxNum = int(float(args[1]))
    else:
        maxNum = 100
    sumAll = sum(range(maxNum+1))
    sumSquares = 0
    for x in range(maxNum+1):
        sumSquares += x**2
    print("Sum squares difference for numbers 1 to "
          + str(maxNum) + " is " + str(sumAll**2-sumSquares))

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


main(sys.argv)
