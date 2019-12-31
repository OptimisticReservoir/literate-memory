#!/usr/bin/env python3
# Project Euler problem 09 with added challenge
# https://www.reddit.com/r/math/comments/ehth9f/dear_mathematicians_of_reddit_i_need_ur_help/
# Given three positive integers a, b and c such that a² + b² - c² = 1.
# Let the number of unique triangles formed with sides a, b and c
# with perimeter less or equal than 50 million represent the surface area
# of an ellipsoid of axes lengths n, 2n and 3n.
# The password is the square of the ceiled positive solution of n.


import sys

from functions import cast_number
#from functions import find_pythagorean_triple


def main(args):
    # arg_f(argument_list, index, validity_function, default_value)
    arg_f = lambda a, i, f, d: f(a[i]) if len(a)>i and f(a[i]) != None else d
    max_index = arg_f(args,1,cast_number,50000000) # 50 million
    bastard_num = count_pythagorean_bastards(max_index)
    print(f"Number of bastards below {max_index} is {bastard_num}")


def count_pythagorean_bastards(i=1000):
    b_list = list_pythagorean_bastards(i)
    print_pythagorean_bastard_list(b_list)
    return len(b_list)

def list_pythagorean_bastards(index_limit):
    """
    Counts Pythagorean bastards with a given index.

    Pythagorean bastards triples that are off by 1 such that:
    a**2 + b**2 = c**2 + 1

    i = index, or sum of a, b, and c (integer)

    Currently it is only set up to find a single triple per index.
    If more are needed, just append them to a list instead.

    It uses formulas from p09.py:
    let x = avg(a,b)
    let y be an offset from x.
    (x-y)**2 + (x+y)**2 = c**2 + 1
    Solving for y gives:
    y**2 = ((1 + c**2 - 2*x**2)/2)
    """

    pythagorean_bastard_list = []
    for i in range(index_limit):
        for c in range(int(i/2 - 0.5*i**0.5 + 1),int(i*0.366),-1):
            """
            Starting range logic:
            a + b + c = index
            a**2 + b**2 = c**2 + 1

            c is at most index/2
            but that would mean a = 1, b = c. trivial.
            We want a < b < c and all integers.
            If b is super large, it could be almost as big as c,
            however, a can't be too tiny because it needs to be
            able to help b**2 become c**2 + 1.
            The smallest a that could do that is (2b+1)**0.5

            In this case, c**2 + 1 = (b+1)**2.
            This means that a**2 + b**2 - 1 = (b+1)**2 = b**2 + 2b + 1
            So, a**2 = 2b+2 --> a = (2b+2)**0.5
            Drop the + 2 to be conservative.

            So b and c will split the loss of (2b)**0.5
            b is trying to be i/2, so the total loss is i**0.5.
            Split each way that is 0.5*i**0.5
            c must be bigger than b, hence the +1.

            The largest c can be is therefore int(i/2 - 0.5*i**0.5 + 1)

            If a=b, then c is a minimum.
            a**2 + a**2 = c**2 + 1
            Solving for c with a+b+c=i gives:
            https://www.wolframalpha.com/input/?i=0+%3D+2c%5E2+%2B+2*c*i+-+i%5E2%2B2%3B+solve+for+c&assumption=%22i%22+-%3E+%22Variable%22
            c = 0.5*(3*i**2-4)**0.5 - 0.5*i
            Which is basically c = int(0.366*i)

            So the smallest c can be is therefore int(0.366*i)

            With these two range restrictions, the search is much smaller
            from a max of ~50% of i, to a low of ~36.6% of i.
            instead of searching all of i, only about 13.4% is searched.
            Without that calculation, the absolute minimum would be a=b=c => 33%
            """

            """
            It uses formulas from p09.py:
            let x = avg(a,b)
            let y be an offset from x.
            (x-y)**2 + (x+y)**2 = c**2 + 1
            Solving for y gives:
            y**2 = ((1 + c**2 - 2*x**2)/2)
            """
            x = (i - c)/2
            y2 = (1 + c**2 - 2*x**2)/2
            if y2 < 0:
                #can't square root a negative number here.
                continue
            y = y2**0.5
            if 1 + y >= x:
                # can't have a offset larger than average
                # that would give negative values.
                continue
            #print(f"y={y} c={c} x={x} i-c%2/2={((i-c)%2)/2}")
            if y%1 == ((i-c)%2)/2:
                # y = integer if i-c is even, or int + 0.5 if odd.
                pythagorean_bastard_list.append([int(x-y), int(x+y), int(c)])
                # the old minimum was 41.4% of i. Maybe I had more insight last time...
                #if c < 0.414*i:
                #    print("**** Unusually low c value.")
                #    print_pythagorean_bastard(pythagorean_bastard_list[-1],i)
                #break
    return pythagorean_bastard_list

def print_pythagorean_bastard(p_bastard,index):
    p_check = p_bastard[0]**2+p_bastard[1]**2-p_bastard[2]**2==1
    """ Prints out a Pythagorean triple and checks vs an index. """
    print(f"A pythagorean bastard for index of {index} is:")
    print(f"a: {p_bastard[0]}"
      + f" b: {p_bastard[1]}"
      + f" c: {p_bastard[2]}")
    print(f"The sum is {sum(p_bastard)}"
      + f" which is {'valid' if index==sum(p_bastard) else 'not valid'}")
    print(f"The bastard is {'valid' if p_check else 'not valid'}")

def print_pythagorean_bastard_list(p_bastard_list):
    #print(p_bastard_list)
    """ Prints each Pythagorean bastard and checks validity. """
    for p_bastard in p_bastard_list:
        p_check = p_bastard[0]**2+p_bastard[1]**2-p_bastard[2]**2==1
        print(f"Bastard a: {p_bastard[0]}"
          + f" b: {p_bastard[1]}"
          + f" c: {p_bastard[2]}"
          + f" is {'valid' if p_check else 'not valid'}")


main(sys.argv)
