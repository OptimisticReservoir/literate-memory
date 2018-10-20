#!/usr/bin/env python3
# Project Euler problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c,
# for which a**2 + b**2 = c**2
# e.g. 3**2 + 4**2 = 5**2 or 9 + 16 = 25
#
# Find the Pythagorean triplet for which a + b + c = 1000
# Find the product of a*b*c

# I'll use the index approach like I did in problem 4
# notice that it says a < b < c - so a != b or c.

# Notice that c must be less than half the total index.
# If c == index/2, then a must be 0 and b must be index/2 also.
# Therefore c must be less than floor(index/2 - 0.1)

# Also note that after subtracting c from the index,
# we can quickly figure out what is valid.
# if we let x = average of a and b, then x = (index - c)/2
# then we can let a = x - y and b = x + y.
# If x is odd, y will be int + 0.5
# then a**2 + b**2 = 2x**2 + 2y**2

# For a given c, x is fixed.
# So we can set c**2 - 2x**2 = 2y**2 and solve for y.

import sys
import time

def main(args):
    index = 0
    result = [0,0,0]
    if(len(args)>1 and cast_number(args[1])):
        index = int(float(args[1]))
    else:
        index = 1000
    t_start = time.time()
    result = find_pythagorean_triple(index)
    print_pythagorean_triple(result,index)
    t_1 = time.time()
    result = other_find_pythagorean_triple(index)
    print_pythagorean_triple(result,index)
    t_2 = time.time()
    print(f"My solution took {t_1-t_start}"
      + f" and other solution took {t_2-t_1}")


def other_find_pythagorean_triple(i=1000):
    for triple in triple_generator(i):
        if sum(triple) == i:
            #print("(\{x\}/\{y\}) =>"+f" {triple}, {sum(triple)}")
            return triple
    return [0,0,0]

def triple_generator(i=1000):
    # Generates pythagorean triples
    limit = int((i/2)**0.5)+5
    for n in range(limit):
        for m in range(n, limit):
            triple = [m**2 - n**2, 2*m*n, m**2 + n**2]
            if sum(triple) <= i:
                yield [int(m**2 - n**2), int(2*m*n), int(m**2 + n**2)]

def print_pythagorean_triple(p_triple,index):
    print(f"A pythagorean triple for index of {index} is:")
    print(f"a: {p_triple[0]}"
      + f" b: {p_triple[1]}"
      + f" c: {p_triple[2]}")
    print(f"The sum is {sum(p_triple)}"
      + f" which is {'valid' if index==sum(p_triple) else 'not valid'}")
    print(f"The product is {list_product(p_triple)}")

def find_pythagorean_triple(i=1000):
    pythagoreanTriple = [0,0,0]
    for c in range(int(i/2 - 0.1),1,-1):
        x = (i - c)/2
        y2 = ((c**2 - 2*x**2)/2)
        if y2 < 0:
            #can't square root a negative number here.
            continue
        y = y2**0.5
        #print(f"y={y} c={c} c%2/2={(c%2)/2}")
        if y%1 == (c%2)/2:
            # y = integer if c is even, or int + 0.5 if odd.
            pythagoreanTriple = [int(x-y), int(x+y), int(c)]
            break
    return pythagoreanTriple

def list_product(list):
    val = 1
    for x in list:
        val *= int(x)
    return val

def cast_number(n):
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
