def is_isogram(string):
    string = string.lower()
    letras = []
    exceptions = (" ", "-")
    for i in string:
        if i in exceptions:
            pass
        elif i not in letras:
            letras.append(i)
        else:
            return False
    return True

print(is_isogram("Emily Jung Schwartzkopf"))