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
