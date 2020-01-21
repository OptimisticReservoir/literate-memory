#!/usr/bin/env python3
# Project Euler problem __
# Explanation ...


import sys

from functions import cast_number

def main(args):
    # arg_f(argument_list, index, validity_function, default_value)
    arg_f = lambda a, i, f, d: f(a[i]) if len(a)>i and f(a[i]) != None else d
    ARGUMENT1 = arg_f(args,1,cast_number,"default 1")
    ARGUMENT2 = arg_f(args,2,cast_number,"default 2")
    ARGUMENT3 = arg_f(args,3,cast_number,"default 3")

main(sys.argv)
