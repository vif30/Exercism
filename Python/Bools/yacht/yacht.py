# Score categories.
# Change the values as you see fit.

YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11

def score(dice, category):
    if category == 0:
        counted = dice.count(dice[0])
        if counted == 5:
            return 50
        return 0
    if category == 1:
        counted = dice.count(1)
        return counted * 1
    if category == 2:
        counted = dice.count(2)
        return counted * 2
    if category == 3:
        counted = dice.count(3)
        return counted * 3
    if category == 4:
        counted = dice.count(4)
        return counted * 4
    if category == 5:
        counted = dice.count(5)
        return counted * 5
    if category == 6:
        counted = dice.count(6)
        return counted * 6
    if category == 7:
        dice.sort()
        counted = dice.count(dice[1]) + dice.count(dice[3])
        if counted == 5:
            return dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
        return 0
    if category == 8:
            dice.sort()
            counted = dice.count(dice[0]) 
            counted1 = dice.count(dice[4])
            if counted == 4:
                return dice[0] * 4
            if counted1 == 4:
                return dice[4] * 4
            if counted == 5 or counted1 == 5:
                return dice[0] * 4
            return 0
    if category == 9:
        ls = [1,2,3,4,5]
        dice.sort()
        if dice == ls:
            return 30
        return 0
    if category == 10:
        bs = [2,3,4,5,6]
        dice.sort()
        if dice == bs:
            return 30
        return 0
    if category == 11:
        counted = dice[0]
        if counted != 5:
            return dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
        return 0