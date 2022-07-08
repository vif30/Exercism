from math import sqrt
def score(x, y):
    h = round(sqrt((x ** 2) + (y ** 2)), 2)
    if(h <= 1):
        return 10
    if(h > 1 and h <= 5):
        return 5
    if(h > 5 and h <= 10):
        return 1
    else:
        return 0
