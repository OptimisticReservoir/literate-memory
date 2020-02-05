#!/usr/bin/env python3
# Project Euler problem __
# Explanation ...


import sys

from functions import cast_number

def main(args):
    # arg_f(argument_list, index, validity_function, default_value)
    arg_f = lambda a, i, f, d: f(a[i]) if len(a)>i and f(a[i]) != None else d
    initial_value = arg_f(args,1,cast_number,1000000) #1 million
    #print_step = arg_f(args,2,cast_number,200)
    factor = arg_f(args,2,cast_number,0.5)
    power = arg_f(args,3,cast_number,0.5)

    desired_print_steps = 10

    value = initial_value
    steps = 0
    #print_step = int(initial_value**(1-power)/((1-power)*factor*desired_print_steps))
    print_step = int((1+2*power)*initial_value**(1-power)/(factor*desired_print_steps))
    print_step *= 2 if power>1 else 1
    print_step -= 1 if power>1 else 0
    if print_step <= 1:
        print_step = 1
    print("Parameters")
    print(f"Intial Value: {initial_value}")
    print(f"Reduction factor: {factor}")
    print(f"Power: {power}")
    print(f"First step reduction: {factor*value**(power-1)}")

    while(value**power > 0.01*initial_value**power):
        print(f"{round(initial_value):.1e} down to {round(value):.1e} " +
        f"after {steps:2} steps of {print_step}. "+
        f"Current {round(value):.2e}**{power}={round(value**power)}")
        steps += 1
        for i in range(print_step):
            value -= factor*value**power
            if value < 0:
                value = 0
                break
    print(f"{round(initial_value):.1e} down to {round(value):.1e} " +
    f"after {steps:2} steps of {print_step}. ")


main(sys.argv)
