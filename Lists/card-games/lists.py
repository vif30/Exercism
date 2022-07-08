"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""
import math

def get_rounds(number):
    number = number // 1
    rounds = [number, number + 1, number + 2]
    return rounds


def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    return bool(number in rounds)


def card_average(hand):
    length = len(hand)
    value = 0
    for i in hand:
        value +=i
    average = value / length
    return average


def approx_average_is_average(hand):
    average = card_average(hand)
    first = hand[0]
    last = hand[len(hand) - 1]
    firstAndLast = (first + last) / 2
    middle = hand[math.ceil(len(hand) / 2) - 1]
    return bool(average == firstAndLast or average == middle)


def average_even_is_average_odd(hand):
    length = len(hand)
    even = 0
    evencont = 0
    odd = 0
    oddcont = 0
    for i in range(0, length, 2):
        evencont += 1
        even += hand[i]
    for i in range(1, length, 2):
        oddcont += 1
        odd += hand[i]
    return bool(even/evencont == odd/oddcont)


def maybe_double_last(hand):
    last = hand[len(hand) - 1]
    if(last == 11):
        hand[len(hand) - 1] = 22
    return hand
