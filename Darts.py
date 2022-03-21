"""System module."""
from math import sqrt
"""Función que recibe unas coordenadas x e y y calcula la puntuación de dicho lanzamiento.
Si la hipotenusa del triangulo que forman las coordenadas con el centro del circulo es <= 1 la puntuacion es 10,
si es entre 1 y 5 será de 5 puntos, si es de entre 5 y 10, se asignara 1 punto y si es mayor a estos, sera 0 puntos"""
def score(x, y):
  """Method Docs."""
    h = round(sqrt((x ** 2) + (y ** 2)), 2)
    if(h <= 1):
        return 10
    if(h > 1 and h <= 5):
        return 5
    if(h > 5 and h <= 10):
        return 1
    else:
        return 0
