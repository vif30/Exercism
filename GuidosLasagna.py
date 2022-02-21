"""System module."""
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(tiempo):
    """
    Devuelve el tiempo de coccion restante
    Esta función calcula el tiempo que le queda a la lasaña para terminar de cocinarse
    """
    remaining = EXPECTED_BAKE_TIME - tiempo
    return remaining

def preparation_time_in_minutes(layers):
    """
    Devuelve el tiempo de preparacion de todas las capas
    Esta funcion devuelve el tiempo que tardaremos el preparar todas la capas de la lasaña
    """
    minutes = layers * PREPARATION_TIME
    return minutes

def elapsed_time_in_minutes(layers, minutes):
    """
    Calculamos el tiempo total de cocina utilizado en la lasaña es decir
    el tiempo de preparacion mas el tiempo que lleva la lasaña en el horno
    """
    time = preparation_time_in_minutes(layers) + minutes
    return time
