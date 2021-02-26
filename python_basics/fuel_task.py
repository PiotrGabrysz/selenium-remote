def calculate_fuel(mass):
    if type(mass) != int:
        return False

    if mass < 0:
        return False
    elif mass == 0:
        return 0
    else:
        fuel = mass//3 - 2
        return fuel
