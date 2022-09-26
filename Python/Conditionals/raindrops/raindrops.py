def convert(number):
    str_numb = ""
    print(number % 5)
    if number % 3 == 0:
        str_numb += "Pling"
    if number % 5 == 0:
        str_numb += "Plang"
    if number % 7 == 0:
        str_numb += "Plong"
    if str_numb == "":
        return str(number)
    return str_numb

