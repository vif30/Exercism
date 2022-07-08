vowels = ("a", "e", "i", "o", "u", "xr", "yt")
consonants = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z", "y")
consonants_cluster = ("bl", "cl", "fl", "gl", "pl", "sl", "br", "cr", "dr", "fr", "gr", "pr", "tr", "sc", "sk", "sm", "sn", "sp", "st", "sw", "tw", "rh", "ch", "qu", "th")
triconsonants_cluster = ("thr", "sch")
def translate(text):
    phrase = text.split()
    pig_latin = ""
    for i in phrase:
        if vowel(i):
            if pig_latin != "":
                pig_latin += " "
            pig_latin += i + "ay"
        if consonant_qu(i):
            if pig_latin != "":
                pig_latin += " "
            texto = i[3:len(i)] + i[0] + i[1] + i[2] + "ay"
            pig_latin += texto
        if consonant_sound(i):
            if pig_latin != "":
                pig_latin += " "
            texto = i[1:len(i)] + i[0] + "ay"
            pig_latin += texto
        if triconsonant_cluster(i):
            if pig_latin != "":
                pig_latin += " "
            texto = i[3:len(i)] + i[0] + i[1] + i[2] + "ay"
            pig_latin += texto
        if consonant_cluster(i):
            if pig_latin != "":
                pig_latin += " "
            texto = i[2:len(i)] + i[0] + i[1] + "ay"
            pig_latin += texto
    return pig_latin
def vowel(word):
    if word.startswith(vowels):
        return True
def consonant_sound(word):
    if word.startswith(consonants) and not word.startswith(consonants_cluster) and not word.startswith("qu", 1) and not word.startswith(vowels):
        return True
def consonant_cluster(word):
    if word.startswith(consonants) and word.startswith(consonants_cluster) and not word.startswith(triconsonants_cluster):
        return True
def triconsonant_cluster(word):
    if word.startswith(consonants) and word.startswith(triconsonants_cluster):
        return True
def consonant_qu(word):
    if word.startswith(consonants) and word.startswith("qu", 1):
        return True
print(translate("yttria"))