"""System module."""
def value_of_card(card):
    """Method Docs."""
    kqj = ["K","Q","J"]
    numbers = ["2","3","4","5","6","7","8","9","10"]
    if card in kqj:
        return 10
    if card == "A":
        return 1
    if card in numbers:
        return int(card)
    return None
def higher_card(card_one, card_two):
    """Method Docs."""
    puntos1 = value_of_card(card_one)
    puntos2 = value_of_card(card_two)
    if puntos1 > puntos2:
        return card_one
    if puntos1 < puntos2:
        return card_two
    if puntos1 == puntos2:
        return card_one, card_two
    return None
def value_of_ace(card_one, card_two):
    """Method Docs."""
    if card_two == "A":
        puntos = value_of_card(card_one) + 11
    else:
        puntos = value_of_card(card_one) + value_of_card(card_two)
    if puntos < 11:
        return 11
    if puntos > 11:
        return 1
    return None
def is_blackjack(card_one, card_two):
    """Method Docs."""
    if card_one == "A" and card_two == "A":
        puntos = 12
        return bool(puntos == 21)
    if card_one == "A" and card_two != "A":
        puntos = 11 + value_of_card(card_two)
        return bool(puntos == 21)
    if card_one != "A" and card_two == "A":
        puntos = 11 + value_of_card(card_one)
        return bool(puntos == 21)
    else:
        puntos = value_of_card(card_one) + value_of_card(card_two)
        return bool(puntos == 21)
    return None
def can_split_pairs(card_one, card_two):
    """Method Docs."""
    return bool(value_of_card(card_one) == value_of_card(card_two))
def can_double_down(card_one, card_two):
    """Method Docs."""
    doblar = [9, 10, 11]
    if card_one == "A" and card_two == "A":
        puntos = 12
        return bool(puntos in doblar)
    else:
        puntos = value_of_card(card_one) + value_of_card(card_two)
        return bool(puntos in doblar)
    return None
