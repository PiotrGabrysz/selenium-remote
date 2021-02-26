class Calculator:

    def __init__(self, dumb_value):
        self.dumb_value = dumb_value

    def add_values(self, a, b):
        return a + b


calculator = Calculator("test")
result = calculator.add_values(1, 2)
print(result)