"""System module."""
def capitalize_title(title):
    """Method Docs."""
    cap = title.title()
    return cap

def check_sentence_ending(sentence):
    """Method Docs."""
    return bool(sentence.endswith("."))

def clean_up_spacing(sentence):
    """Method Docs."""
    cap = sentence.strip()
    return cap

def replace_word_choice(sentence, old_word, new_word):
    """Method Docs."""
    cap = sentence.replace(old_word, new_word)
    return cap
