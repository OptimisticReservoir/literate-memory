#!/usr/bin/env python3
# Project Euler problem 6
# Find the sum square difference of numbers 1 to 100.
# e.g. For numbers 1 to 3 it is (1+2+3)**2 - (1**2 + 2**2 + 3**2)

import sys

from functions import cast_number
from functions import sum_square_difference

def main(args):
    maxNum = 0
    if(len(args)>1 and cast_number(args[1])):
        maxNum = int(float(args[1]))
    else:
        maxNum = 100
    numList = [*range(maxNum+1)]
    ssd = sum_square_difference(numList)
    print("Sum squares difference for numbers 1 to "
          + f"{maxNum} is {ssd}")

main(sys.argv)
