#!/usr/bin/env python3
# Project Euler Problem 7
# Find the 10001st prime number
# e.g. First 6 are: 2, 3, 5, 7, 11, 13. So 6th is 13.


import sys
from functions import ordinal
from functions import cast_number
from functions import get_boolstring
#from functions import is_boolstring
from functions import generate_n_primes

def main(args):
    # arg_f(argument_list, index, validity_function, default_value)
    arg_f = lambda a, i, f, d: f(a[i]) if len(a)>i and f(a[i]) != None else d
    nthPrime = arg_f(args,1,cast_number,10001)
    # get_boolstring is fine, because if it gets False, that's default anyway.
    print_results = arg_f(args,2,get_boolstring,False) 
    primes = generate_n_primes(nthPrime)
    if print_results:
        for p in primes:
            print(p)
    print("The " + str(nthPrime) + ordinal(nthPrime)
          + " is " + str(primes[-1]))

main(sys.argv)
