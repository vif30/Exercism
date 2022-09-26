import string
PLAIN = string.ascii_lowercase
CIPHER = "".join(reversed(string.ascii_lowercase))
IGNORE = (" ", ",", ".")
def encode(plain_text):
    plain_text = plain_text.lower()
    ciphered= ""
    counter = 0
    for i in plain_text:
        if i in IGNORE:
            continue
        if counter % 5 == 0 and counter != 0:
            ciphered += " "
        index = PLAIN.find(i)
        if index == -1 and i not in IGNORE:
            ciphered += i
        else:
            ciphered += CIPHER[index]
        counter += 1
    return ciphered

def decode(ciphered_text):
    ciphered_text = ciphered_text.lower()
    plain = ""
    for i in ciphered_text:
        index = CIPHER.find(i)
        if i in IGNORE:
            continue
        if index == -1:
            plain += i
        else:
            plain += PLAIN[index]
    return plain
