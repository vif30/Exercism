def value(colors):
    values = {"black":"0", "brown":"1", "red":"2", "orange":"3", "yellow":"4", "green":"5", "blue":"6", "violet":"7", "grey":"8", "white":"9"}
    number = values[colors[0]] + values[colors[1]]
    return int(number)
