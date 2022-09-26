"""System module."""
def is_criticality_balanced(temperature, neutrons_emitted):
    """Method Docs."""
    return bool(temperature < 800 and neutrons_emitted > 500 and temperature*neutrons_emitted < 500000)

def reactor_efficiency(voltage, current, theoretical_max_power):
    """Method Docs."""
    generated_power = voltage * current
    percentage = (generated_power/theoretical_max_power) * 100
    if percentage >= 80:
        return "green"
    if 80 > percentage >= 60:
        return "orange"
    if 60 > percentage >= 30:
        return "red"
    return "black"

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Method Docs."""
    ninety = (90 * threshold) / 100
    cientodie = (110 * threshold) / 100
    tempneu = temperature * neutrons_produced_per_second
    if tempneu < ninety:
        return "LOW"
    if ninety <= tempneu < cientodie:
        return "NORMAL"
    return "DANGER"
