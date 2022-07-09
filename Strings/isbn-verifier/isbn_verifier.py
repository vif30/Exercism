import string
def is_valid(isbn):
    if len(isbn) < 9:
        return False
    clean_isbn = clean(isbn)
    if not clean_isbn:
        return False
    return validate(clean_isbn)
def clean(isbn):
    numbers = []
    clean = []
    for i in isbn:
        if i == "-":
            pass
        else: 
            numbers.append(i)
    if numbers[len(numbers)-1] == "X":
        numbers.pop()
        numbers.append("10")
    if numbers[len(numbers)-1] in list(string.ascii_uppercase):
        return False
    for j in numbers:
        if j in list(string.ascii_uppercase):
            return False
        else:
            clean.append(int(j))
    if len(clean) != 10:
        return False
    else:
        return clean
def validate(clean_isbn):
    val_isbn = (clean_isbn[0] * 10 + clean_isbn[1] * 9 + clean_isbn[2] * 8 + clean_isbn[3] * 7 + clean_isbn[4] * 6 + clean_isbn[5] * 5 + clean_isbn[6] * 4 + clean_isbn[7] * 3 + clean_isbn[8] * 2 + clean_isbn[9] * 1) % 11
    if val_isbn == 0:
        return True
    else:
        return False
