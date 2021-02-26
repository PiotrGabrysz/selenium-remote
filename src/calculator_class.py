class Calculator:

    def __init__(self, dumb_value):
        self.dumb_value = dumb_value

    def add_values(self, a, b):
        try:
            return a + b
        except TypeError as e:
            print(e)
            return False

    def multiply_values(self, a, b):
        return a * b

    def substract_values(self, a, b):
        return a - b

    def divide_values(self, a, b):
        if b == 0:
            return False
        return a / b

