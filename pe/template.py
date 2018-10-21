#!/usr/bin/env python3
# Project Euler problem __
# Explanation ...


import sys

from functions import cast_number

def main(args):
    ARGUMENT = 0
    if(len(args)>1 and cast_number(args[1])):
        # Use passed arguments
        ARGUMENT = int(float(args[1]))
    else:
        # Use default parameters
        ARGUMENT = 1

main(sys.argv)
