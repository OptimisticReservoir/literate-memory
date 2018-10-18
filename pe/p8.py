#!/usr/bin/env python3



import sys

def main(args):
    if(len(args)>1):
        # Use passed arguments
    else:
        # Use default parameters

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
