#!/usr/bin/env python3
# Project Euler problem 5
# find the smallest number evenly divisible by all numbers 1-20.
# e.g. 2520 is the smallest number evenly divisible by 1 though 10.

import sys

from functions import lcm
from functions import cast_number

def main(args):
    maxNum = 0
    if(len(args)>1 and cast_number(args[1])):
        maxNum = int(float(args[1]))
    else:
        maxNum = 20
    lowest_common_multiple = lcm([*range(2,maxNum+1)])
    print("Lowest common multiple of all integers 1 to "
          + f"{maxNum} is {lowest_common_multiple}")

main(sys.argv)
