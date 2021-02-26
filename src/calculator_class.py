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

    def get_n_fibonacci(self, n):
        a_1, a_2 = 0, 1
        if n > 2:
            for i in range(n - 2):
                a_1, a_2 = a_2, a_1 + a_2
            return a_2
        elif n == 2:
            return a_2
        elif n == 1:
            return a_1
        else:
            return False

    def factorial(self, n):
        if type(n) != int:
            return False
        if n > 0:
            result = 1
            for i in range(1, n + 1):
                result *= i   # result = result * i
            return result
        elif n == 0:
            return 1
        else:
            return False