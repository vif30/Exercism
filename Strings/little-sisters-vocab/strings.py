"""System module."""
def add_prefix_un(word):
    """Module docs.
    Función que añade el prefijo un a la palabra que le pasen"""
    unword = 'un' + word
    return unword
def make_word_groups(vocab_words):
    """Module docs.
    Función que recorre un array de palabras, donde la primera es un prefijo
    al que hay que añadir al resto, lee dicho prefijo y crea un string
    donde lo añade al resto de palabras mediante el separador :: """
    strings = ''
    for i, word in enumerate(vocab_words):
        if i==0:
            strings+= word
        else:
            strings += ' :: ' + vocab_words[0] + word
    return strings
def remove_suffix_ness(word):
    """Module docs.
    Función que recibe una palabra con sufijo -ness y devuelve la palabra
    eliminando dicho sufijo, en caso de que esta acabe en consonante + i,
    se sustituye dicha i por una y."""
    letras = len(word)-4
    word2 = word[0:letras]
    if(word2[letras-1] == 'i' and word2[letras - 2] not in ['a','e','i','o','u']):
        word2 = word2[0:letras-1] + 'y'
    return word2
def noun_to_verb(sentence, index):
    """Module docs.
    Función que recibe una frase y un índice, esta separa la frase en un array de palabras
    y coge la palabra que se encuentra en la posicion del índice y le añade el sufijo -en,
    tiene en cuenta si al final de dicha palabra tiene una coma, punto o exclamación."""
    separado = sentence.split()
    word = separado[index]
    wordlen = len(word) - 1
    if(word[wordlen] in [',', '.', '!']):
        word = word[0:wordlen]
    word = word + 'en'
    return word
