def calculate_fuel(mass):
    if type(mass) != int and type(mass) != float:
        return False

    if mass < 0:
        return False
    elif mass == 0:
        return 0
    elif mass < 3:
        return 1
    else:
        fuel = mass//3 - 2
        return fuel
