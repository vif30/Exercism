"""System module."""
"""Metodo que segun el string que le pasemos, devuelve una constestación diferente."""
def response(hey_bob):
    """Method Docs."""
    hey_bob = hey_bob.strip() #Eliminamos los espacios en blanco del principio y del final del string
    if(hey_bob.endswith("?") and not hey_bob.isupper()):
      #Si es una pregunta y no esta en mayusculas
      return "Sure."
    if(hey_bob.isupper() and not hey_bob.endswith("?")):
      #Si esta mayusculas y no es una pregunta
      return "Whoa, chill out!"
    if(hey_bob.endswith("?") and hey_bob.isupper()):
      #Si es una pregunta y ademas esta en mayusculas
       return "Calm down, I know what I'm doing!"
    if(not hey_bob):
      #Si enviamos un string vacio
       return "Fine. Be that way!"
    else:
      #Para el resto de posibilidades
      return "Whatever."   
