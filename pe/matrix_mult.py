#!/usr/bin/env python3
# Project Euler problem __
# Explanation ...


import sys
import numpy as np

from functions import cast_number

def main(args):
    # arg_f(argument_list, index, validity_function, default_value)
    arg_f = lambda a, i, f, d: f(a[i]) if len(a)>i and f(a[i]) != None else d
    unique_cards = arg_f(args,1,cast_number,9)
    bm_weeks = arg_f(args,2,cast_number,24)
    ARGUMENT3 = arg_f(args,3,cast_number,"default 3")

    card_draw_list = np.eye(bm_weeks,1)
    for j in range(unique_cards):
        unique_p = (unique_cards - j)/unique_cards
        prob_dist = geo_dist(unique_p,bm_weeks)
        print(f"Week {j} gives a prob_dist of:")
        print(prob_dist)
        xform_mat = np.mat(build_stair_matrix(prob_dist, bm_weeks))
        card_draw_list = xform_mat @ card_draw_list
        print(f"Week {j} gives a card list of:")
        print(card_draw_list)
        print(f"Week {j} gives a prob_dist of:")
        print(xform_mat)
        wait = input("PRESS ENTER TO CONTINUE.")

def geo_dist(p,n):
    g_dist = []
    for i in range(n):
        g_dist.append(p*(1-p)**i)
    return g_dist

def build_stair_matrix(step_array_ref,stair_width):
    # don't change the original
    step_array = step_array_ref
    stair_matrix = []
    for i in range(stair_width):
        stair_matrix.append(step_array)
        # Shift the array down 1 with a leading 0.
        step_array.pop()
        step_array.insert(0,0)
    return stair_matrix

def list_shift_replace(list_ref, shifts, new_val=0):
    #don't change the original
    list = list_ref
    for i in range(shifts):
        list.insert(0,new_val)
        list.pop()
    return list

main(sys.argv)
