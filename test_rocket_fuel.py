import unittest
from python_basics.fuel_task import calculate_fuel
from hamcrest import *


class TestRocket(unittest.TestCase):

    def test_mass_12(self):
        assert_that(calculate_fuel(12), equal_to(2))

    def test_high_fuel(self):
        assert_that(calculate_fuel(100756), equal_to(33583))

    def test_negative_value(self):
        assert_that(calculate_fuel(-10), equal_to(False))

    def test_no_fuel(self):
        assert_that(calculate_fuel(0), equal_to(0))

    def test_string_value(self):
        assert_that(calculate_fuel("test"), equal_to(False))


if __name__ == '__main__':
    unittest.main()
