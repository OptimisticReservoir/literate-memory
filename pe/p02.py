#!/usr/bin/env python3
# Project Euler Problem 2
# Sum the even Fibonacci values below 4 million
# First ten terms are 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

def Fib(a,b):
    return a+b


x = 1
y = 2
z = 0
evenSum = 0
maxFib = 4000000

while(y < maxFib):
    evenSum += y if not y%2 else 0
    z = Fib(x,y)
    x = y
    y = z

print(evenSum)

