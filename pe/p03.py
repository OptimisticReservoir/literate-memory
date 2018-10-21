#!/usr/bin/env python3
# Project Euler problem 3
# Find largest prime factor of 600851475143

import sys

from functions import cast_number
from functions import LPF

def main(args):
    if(len(args)>1 and cast_number(args[1])):
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



main(sys.argv)
