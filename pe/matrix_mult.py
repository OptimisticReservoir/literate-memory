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

    card_draw_list = np.eye(bm_weeks,1)
    chance_to_get_cards = []
    weeks_to_get_cards = []
    weeks_to_get_cards_probability_cutoff = 0.8
    for j in range(unique_cards):
        unique_p = (unique_cards - j)/unique_cards
        prob_dist = geo_dist(unique_p,bm_weeks)
        # prob_dist = list_shift_replace(geo_dist(unique_p,bm_weeks),j)
        # print(f"Week {j} gives a prob_dist of:")
        # print(prob_dist)
        xform_mat = np.mat(build_stair_matrix(prob_dist, bm_weeks))
        card_draw_list = xform_mat.T @ card_draw_list
        if j > 0:
            card_draw_list = np.mat(list_shift_replace(card_draw_list.tolist(),1,[0]))
        # XXX: experimental data below.
        # if j == 2 or j == 4: # problems getting the second and fourth card.
        #    card_draw_list = np.mat(list_shift_replace(card_draw_list.tolist(),1,[0]))
        chance_to_get_this_card = card_draw_list.sum().round(3)
        chance_to_get_cards.append(f"{'' if 100 * chance_to_get_this_card == 100 else ' '}{100 * chance_to_get_this_card:.1f}%")
        weeks_to_get_this_card = list_cumsum_threshold(card_draw_list.T.tolist()[0],weeks_to_get_cards_probability_cutoff)
        weeks_to_get_cards.append("Unlikely" if weeks_to_get_this_card == -1 else weeks_to_get_this_card + 1) # array starts at 0.
        print(f"Chance to get card {j+1}: {chance_to_get_cards[j]}. Weeks: {weeks_to_get_cards[j]}")
        #print(f"{j+1}: {card_draw_list.round(2).T}")
        #print(f"Card {j+1} gives a card_draw_list of: {card_draw_list.round(3).T}")
        # print(f"Week {j} gives a xform_mat of:")
        # # print(xform_mat)
        #
        # wait = input("PRESS ENTER TO CONTINUE.")
    print(f"Total chance to find all cards before season end: {chance_to_get_cards[unique_cards-1]}")

def geo_dist(p,n):
    g_dist = []
    for i in range(n):
        g_dist.append(p*(1-p)**i)
    return g_dist

def build_stair_matrix(step_array_ref,stair_width):
    # don't change the original
    step_array = step_array_ref.copy()
    stair_matrix = []
    for i in range(stair_width):
        stair_matrix.append(step_array.copy())
        # print(np.mat(stair_matrix))
        # wait = input("PRESS ENTER TO CONTINUE.")
        # Shift the array down 1 with a leading 0.
        step_array.pop()
        step_array.insert(0,0)
    return stair_matrix

def list_shift_replace(list_ref, shifts, new_val=0):
    #don't change the original
    list = list_ref.copy()
    for i in range(shifts):
        list.insert(0,new_val)
        list.pop()
    return list

def list_cumsum_threshold(list,threshold):
    #print(list)
    threshold_not_reached = -1
    cumsum = 0
    for i in range(len(list)):
        cumsum += list[i]
        #print(f"{cumsum} and {list[i]}")
        if cumsum >= threshold:
            return i
    return threshold_not_reached


main(sys.argv)
