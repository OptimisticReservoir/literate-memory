#!/usr/bin/env python3
# Project Euler problem __
# Explanation ...


import sys
from math import log

from functions import cast_number

def main(args):
    # arg_f(argument_list, index, validity_function, default_value)
    arg_f = lambda a, i, f, d: f(a[i]) if len(a)>i and f(a[i]) != None else d
    probability = arg_f(args,1,cast_number,0.8)
    sensitivity = arg_f(args,2,cast_number,0.1)
    i_limit = arg_f(args,3,cast_number,100) # guess
    i_limit_old = 0
    p_sum = 0

    while (abs(i_limit_old - i_limit) > (0.01+sensitivity)/2*i_limit):
        #print(f"Old:{round(i_limit_old)} New:{round(i_limit)}")
        i_limit_old = i_limit
        i_limit = (log(sensitivity) - log(i_limit))/log(probability)
    print(f"The test limit for {probability} is {round(i_limit)}")

    for i in range(int(i_limit)):
        x = (i+1)*(1-probability)*probability**i
        p_sum += x
        #print(f"{i}: {round(x,2)}")

    print(f"Average value is {round(p_sum,1)}")

main(sys.argv)
