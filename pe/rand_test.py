#!/usr/bin/env python3
# Project Euler problem __
# Explanation ...


import sys

from functions import cast_number
from my_random import MyRNG

def static_test():
    if "x" not in static_test.__dict__:
        static_test.x = 0
    static_test.x += 1
    print(static_test.x)

def main(args):
    # arg_f(argument_list, index, validity_function, default_value)
    arg_f = lambda a, i, f, d: f(a[i]) if len(a)>i and f(a[i]) != None else d
    ARGUMENT1 = arg_f(args,1,cast_number,"default 1")
    ARGUMENT2 = arg_f(args,2,cast_number,"default 2")
    ARGUMENT3 = arg_f(args,3,cast_number,"default 3")
    r = MyRNG()
    for x in range(500):
        i = r.rand_range(365)
        print(f"{i} {'Winning ****' if i == 0 or i == 364 else ''}")

main(sys.argv)
