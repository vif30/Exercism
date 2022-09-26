def square_of_sum(number):
    sum = 0
    for i in range(number):
        sum += i+1
    sum = pow(sum, 2)
    return sum


def sum_of_squares(number):
    square = 0
    for i in range(number):
        square += pow(i+1,2)
    return square


def difference_of_squares(number):
    difference = square_of_sum(number) - sum_of_squares(number)
    return difference
