#!/usr/bin/env python3
# Project Euler problem 8
# Find the 13 adjacent digits that have the greatest product
# They must come from the 1000 digit number below, "nums"
# e.g. the 4 digits with the largest product are 9x9x8x9 = 5832

import sys

nums = '''
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
'''
nums = nums.replace('\n','') #Make it one complete number.

def main(args):
    digits = 0
    if(len(args)>1 and cast_number(args[1])):
        digits = int(float(args[1]))
    else:
        digits = 13
    print(f"{len(nums)} digit number.")
    print(f"Finding the {digits} consecutive digits with the largest product")
    print(max_product_slice(nums,digits))

def max_product_slice(list,size):
    max = 0;
    product = 0;
    for x in range(len(list)-size+1): # size is inclusive, so we need +1
        product = list_product(list[x:x+size])
        if product > max: max = product
    return max

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
