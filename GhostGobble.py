"""System module."""
def eat_ghost(power_pellet_active, touching_ghost):
    """Función que recibe dos booleanos, si ambos son True, devuelve True
    sino, devuelve False"""
    return bool(power_pellet_active and touching_ghost)

def score(touching_power_pellet, touching_dot):
    """Función que recibe dos booleanos, si uno de los dos es True, devuelve True,
    si ninguno es True, devuelve False"""
    return bool(touching_power_pellet or touching_dot)

def lose(power_pellet_active, touching_ghost):
    """Función que recibe dos booleanos, si power_pellet_active = False y
    touching_ghost = False, devuelve True, sino devuelve False"""
    return bool(not power_pellet_active and touching_ghost)

def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Función que recibe 3 booleandos, si has_eaten_all_dots = True y llamando a la función
    lose() con los otros dos = False, devuelve true(es decir, ganamos la partida) sino,
    devuelve False(perdemos)"""
    return bool(has_eaten_all_dots and not lose(power_pellet_active, touching_ghost))
