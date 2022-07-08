def steps(number):
    cont = 0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    while number != 1:
        if (number % 2) == 0:
            number = number / 2
            cont += 1
        else: 
            number = number * 3 + 1
            cont += 1
    return cont