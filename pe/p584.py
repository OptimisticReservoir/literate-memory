#!/usr/bin/env python3
# Project Euler problem __
# Birthday problem revisted
# Examples:
# number of people in room before
# 3 people have birthdays within
# 1 day of each other: 10 day year
# Answer: 5.78688636
# number of people in room before
# 3 people have birthdays within
# 7 days of each other: 100 day year
# Answer: 8.48967364
# number of people in room before
# 4 people have birthdays within
# 7 days of each other: 365 day year
# Answer: Find it.

import sys
import random

from functions import cast_number

def main(args):
    # arg_f(argument_list, index, validity_function, default_value)
    arg_f = lambda a, i, f, d: f(a[i]) if len(a)>i and f(a[i]) != None else d
    matches = arg_f(args,1,cast_number,4)
    tolerance = arg_f(args,2,cast_number,7)
    year_len = arg_f(args,3,cast_number,365)
    nl = "\n"
    b_days_generator = generate_birthdays(year_len)
    b_days = []
    current_list = []
    match_list = []
    counter = 0
    lengths = []
    for i in b_days_generator:
        b_days.append(i)
        current_list = check_b_day_match(b_days,matches,tolerance,year_len)
        counter += 1
        if current_list:
            match_list.append(b_days.copy())
            b_days.clear()
        if counter>10000: break
    for i in match_list:
        #print(i)
        lengths.append(len(i))
    print(f"Testing scenario needing {matches} matches,{nl}"
    + f"within {tolerance} day period,{nl}"
    + f"in a year {year_len} days long.")
    print(f"After {len(lengths)} trials,"
    + f" the result is {sum(lengths)/len(lengths)}.")
    fd = open("results_584.csv","a")
    run_conditions = f"{matches}_{tolerance}_{year_len}"
    fd.write(f"{run_conditions},{sum(lengths)},{len(lengths)}{nl}")


def is_within_x_wrap(a,b,x=0,mod=0):
    if mod:
        return min((a-b)%mod,(b-a)%mod) <= x
    else:
        return abs(a-b) <= x

def is_x_ahead_wrap(a,b,x=0,mod=0): # b expected to be larger
    if mod:
        return (b-a)%mod <= x
    else:
        return b >= a and b-a <= x

def check_b_day_match(list,matches,tolerance,year_len):
    match_list = []
    for day in list:
        match_list.clear()
        min_day = day # So we keep our reference point.
        for test_day in list:
            #print(f"Day:{day} Min:{min_day} Test:{test_day}")
            if is_x_ahead_wrap(min_day,test_day,tolerance,year_len):
                match_list.append(test_day)
                min_day = min(min(match_list),min_day) # Don't make it bigger
        if len(match_list)>=matches:
            return match_list
    return []

def generate_birthdays(year_len):
    random.seed()
    # r = random.SystemRandom()
    while(1):
        # yield r.randrange(year_len)
        yield random.randrange(year_len)

main(sys.argv)
