# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = None
SUPERLIST = None
EQUAL = None
UNEQUAL = None


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL 
    if list_one in list_two:
        return SUBLIST

print(sublist([1, 2, 5], [0, 1, 2, 3, 1, 2, 5, 6]))