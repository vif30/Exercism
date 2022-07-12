def classify(number):
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    factores = []
    for i in range(1, number):
        if number % i == 0:
            factores.append(i)
    suma = 0
    for j in factores:
        suma += j
    if suma == number:
        return "perfect"
    if suma < number:
        return "deficient"
    if suma > number:
        return "abundant"
