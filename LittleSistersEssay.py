"""System module."""
"""Metodo que cambia la primera letra de todas las palabras de un string por la mayuscula"""
def capitalize_title(title):
    """Method Docs."""
    cap = title.title()
    return cap
  """Metodo que devuelve True si un string termina en "." y False si no"""
def check_sentence_ending(sentence):
    """Method Docs."""
    return bool(sentence.endswith("."))
  """Metodo que elimina los espacios en blanco del principio o del final de un string"""
def clean_up_spacing(sentence):
    """Method Docs."""
    cap = sentence.strip()
    return cap
  """Metodo que cambia una palabra elegida por otra dentro de un string"""
def replace_word_choice(sentence, old_word, new_word):
    """Method Docs."""
    cap = sentence.replace(old_word, new_word)
    return cap
