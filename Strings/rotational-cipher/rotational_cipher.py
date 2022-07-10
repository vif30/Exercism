import string
def rotate(text, key):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    rotated = ""
    for iter in text:
        if iter in upper:
            index = upper.index(iter)
            position = index + key
            if position >= 26:
                position = position - 26
            rotated += upper[position]
        if iter in lower:
            index = lower.index(iter)
            position = index + key
            if position >= 26:
                position = position - 26
            rotated += lower[position]
        if iter not in upper and iter not in lower:
            rotated += iter
    return rotated

