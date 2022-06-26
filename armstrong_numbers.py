def is_armstrong_number(number):
    length = len(str(number))
    arms = 0
    for n in range(length):
        numero = str(number)[n]
        arms += pow(int(numero) ,length)
    if arms == number:
        return True
    else:
        return False