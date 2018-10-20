#!/usr/bin/env python3
# Project Euler Problem 1
# Sum all multiples of 3 or 5 below 1000

x = sum({*range(0,1000,3)}.union({*range(0,1000,5)}))
print("Sum of multiples of 3 or 5 below 1000 is " + str(x))

print("testing:")
y = range(0,10,3)
#print("range(0,10,3) gives " + str(range(0,10,3)))
print("range(0,10,3) gives " + str(y))
#print("*range(0,10,3) gives " + str(*range(0,10,3)))
print("*range(0,10,3) gives:")
print(*y)
print("{*range(0,10,3)} gives " + str({*range(0,10,3)}))
#print("{*range(0,10,3)} gives " + str({*y}))
