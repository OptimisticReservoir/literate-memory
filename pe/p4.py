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




