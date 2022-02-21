"""System module."""
#Función que recibe un presupuesto y un ratio de cambio entre divisas y
#devuelve el total del cambio con la nueva divisa.
def exchange_money(budget, exchange_rate):
    """Method Docs."""
    change = budget / exchange_rate
    return change
#Función que toma un presupuesto máximo y la cantidad que vamos a cambiar
#y devuelve la diferencia entre estos.
def get_change(budget, exchanging_value):
    """Method Docs."""
    lose = budget - exchanging_value
    return lose
#Función que recibe el valor de los billetes y el total de billetes
#y devuelve el valor total.
def get_value_of_bills(denomination, number_of_bills):
    """Method Docs."""
    total_bills = denomination * number_of_bills
    return total_bills
#Función que recibe el presupuesto máximo y el valor de los billetes en los que
#se puede recibir dicho presupuesto y devuelve la cantidad máxima de billetes
#que hay en ese presupuesto (si pres=127.5 y valorbilletes=5 máximo de billetes=25)
def get_number_of_bills(budget, denomination):
    """Method Docs."""
    number_bills = budget / denomination
    number_bills = int(number_bills)
    return number_bills
#Función que recibe el presupuesto, ratio del cambio, porcentaje "untado" y valor de
#los billetes. Aqui calculamos el dinero máximo que podremos sacar al cambiar el presupuesto
#dado en los billetes también dado. Al calcular el cambio le sumaremos al ratio el porcentaje
#de impuesto "untado" y por ultimo dividiremos en el numero maximo posible con el valor de los
#billetes.
def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Method Docs."""
    spr = exchange_rate * spread / 100
    exchange = exchange_money(budget, exchange_rate+spr)
    bills = get_number_of_bills(exchange, denomination)
    maximo = bills * denomination
    return maximo
#Función que calcula la cantidad de dinero que no podremos cambiar por el valor de los billetes
#de cambio.
def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    """Method Docs."""
    exchengable = exchangeable_value(budget, exchange_rate, spread, denomination)
    spr = exchange_rate * spread / 100
    exchange = exchange_money(budget, exchange_rate+spr)
    non = exchange - exchengable
    return int(non)
