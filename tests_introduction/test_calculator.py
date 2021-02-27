import unittest
from tests_introduction.src.calculator_class import Calculator
from hamcrest import *

class TestBasicOperations(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator("test")

    def test_add(self):
        assert_that(self.calculator.add_values(1, 2), equal_to(3))

    def test_div(self):
        assert_that(self.calculator.divide_values(1, 0), equal_to(0))

    def test_sub(self):
        assert_that(self.calculator.substract_values(1, 2), equal_to(-1))

    def test_mul(self):
        assert_that(self.calculator.multiply_values(1, 0), equal_to(0))


class TestFibonacci(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator("test")

    def test_negative_value(self):
        assert_that(self.calculator.get_n_fibonacci(-1), equal_to(False))

    def test_positive_value(self):
        assert_that(self.calculator.get_n_fibonacci(3), equal_to(1))


if __name__ == '__main__':
    unittest.main()
