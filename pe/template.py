#!/usr/bin/env python3
# Project Euler problem __
# Explanation ...


import sys

from functions import cast_number

def main(args):
    c_n = cast_number # shortcut for large lambda to fit on 1 line.
    arg_f = lambda a, i, d: c_n(a[i]) if len(a)>i and c_n(a[i]) else d
    ARGUMENT1 = arg_f(args,1,10)
    ARGUMENT2 = arg_f(args,2,10)
    ARGUMENT3 = arg_f(args,3,10)

main(sys.argv)
