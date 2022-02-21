def square(numero):
    """Función que recibe un número de posición del tablero y devuelve la cantidad
    de granos que se encuentran en dicha posición, maneja las excepciones en caso 
    de lanzar la función con numeros mayores a 64 o menores de 1"""
    if(numero < 1 or numero > 64):
        raise ValueError("square must be between 1 and 64")
    else:
        elevado = numero-1
        granos = 2**elevado
        return granos
    
def total():
    """Función que calcula el total de granos en el tablero, recorre en un for los
    numeros del 1 al 64, sumando al total 2 elevado a i"""
    total = 0
    for i in range(64):
        total += 2**(i)
    return total
