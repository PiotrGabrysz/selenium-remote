from src.calculator_class import Calculator
from src.factorial_method import factorial
import unittest
from hamcrest import *

print(factorial(10))

factorial("1")

calculator = Calculator("test")

calculator.add_values(1, "1")