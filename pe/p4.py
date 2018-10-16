#!/usr/bin/env python3
# Find the largest palindrome made from the product of two 3 digit numbers
# e.g. for two digit numbers: 91 x 99 = 9009 

# I am going to attempt this by using an index or degree or something
# I don't remember the mathematical term, but instead of looping from
# 999 x 999 using a double loop, I'll instead start with an index.
#
# The index is equal to the sum of the two numbers. so 1998 is first.
# then in the second loop, I'll start with min(999,current index).
# then I'll count down until the partner is larger than 999, i.e. not 3 digits.
#
# e.g. when index is 1990, and the second loop is at 990, the partner would be
# 1000 which is a 3 digit number. So the second loop would run from 999 to 990
# for index of 1990.
#
# The benefit is that this will find the largest palindrome first (I think)
# and it will avoid unnecessary calculations, e.g. 909 x 101


import math
import sys

def main(args):
    maxDigits = 0
    palindrome = ProductPalindrome()
    if(len(args)>1 and castNumber(args[1])):
        # Use passed arguments
        maxDigits = int(float(args[1]))
    else:
        # Use default parameters
        maxDigits = 3
    palindrome = findMaxPalindrome(maxDigits)
    print("Largest palindrome with " + str(maxDigits) + " is " +
            str(palindrome.value) + " from " + str(palindrome.x) + 
            " and " + str(palindrome.y) + " and it is " + 
            ("valid." if palindrome.valid else "not valid."))

def findMaxPalindrome(digits):
    digits = int(castNumber(digits))
    if not digits:
        digits = 3 # use 3 as default if invalid digit given.
    maxNum = int("9"*digits) # all 9s is max value
    maxIndex = 2 * maxNum # index = sum of the two numbers to be multipled.
    i = maxIndex
    x = maxNum
    y = maxNum
    solved = False
    # I'm postulating that this will find the maximum palindrome first
    # if not, I'll need to add all palindromes found to a list and then
    # find max later.
    while(i > 0):
        x = maxNum
        y = i - x
        # x + y = i
        while(y <= maxNum):
            if isPalindrome(x*y):
                solved = True
                break
            x -= 1
            y += 1
        if solved:
            break
        i -= 1
    return ProductPalindrome(x,y)

class ProductPalindrome:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.value = x*y
        self.valid = isPalindrome(self.value)

def isPalindrome(s):
    s = str(s)
    i = 0
    while(i < len(s)/2):
        if s[i] != s[-(i+1)]: # 0 is first, -1 is last.
            return False
        i += 1
    return True

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
