def label(colors):
    value = []
    for i in colors:
        if i == "black":
            value.append(0)
        if i == "brown":
            value.append(1)
        if i == "red":
            value.append(2)
        if i == "orange":
            value.append(3)
        if i == "yellow":
            value.append(4)
        if i == "green":
            value.append(5)
        if i == "blue":
            value.append(6)
        if i == "violet":
            value.append(7)
        if i == "grey":
            value.append(8)
        if i == "white":
            value.append(9)
    ohms = str(value[0]) + str(value[1])
    kiloohms = ""
    j = 0
    for j in range(value[2]):
        ohms += "0"
    if ohms[len(ohms)-1] == "0" and ohms[len(ohms)-2] == "0" and ohms[len(ohms)-3] == "0":
        for k in ohms:
            if k != "0":
                kiloohms += k
        return kiloohms + " kiloohms"
    return ohms + " ohms"

print(label(["yellow", "violet", "yellow"]))