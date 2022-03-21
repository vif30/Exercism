"""Función que recibe un año y nos indica si es bisiesto o no,
para ello primero divide el año entre 4, despues entre 100 y 
entre 400, si es divisible entre 4 y 100 no es bisiesto, si
es divisible entre 4 y no entre 100, es bisiesto, y si es
divisible entre 4, 100 y 400 si es bisiesto"""
def leap_year(year):
    h = year % 4
    div4 = bool(h == 0)
    h2 = year % 100
    div100 = bool(h2 == 0)
    h3 = year % 400
    div400 = bool(h3 == 0)
    if(div4 and not div100):
        return True
    if(div4 and div100 and div400):
        return True
    else:
        return False
