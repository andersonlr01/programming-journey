"""Unit tests. Run in VS Code's Testing panel or with: python -m unittest -v"""

import unittest

from calculator import CalculatorError, calculate, format_result


class TestCalculator(unittest.TestCase):
    def test_basic_operations(self):
        self.assertEqual(calculate("+", 2, 3), 5)
        self.assertEqual(calculate("-", 2, 3), -1)
        self.assertEqual(calculate("*", 4, 3), 12)
        self.assertEqual(calculate("/", 9, 3), 3)
        self.assertEqual(calculate("**", 2, 10), 1024)
        self.assertEqual(calculate("%", 10, 3), 1)
        self.assertEqual(calculate("sqrt", 16), 4)

    def test_division_by_zero(self):
        with self.assertRaises(CalculatorError):
            calculate("/", 1, 0)

    def test_modulo_by_zero(self):
        with self.assertRaises(CalculatorError):
            calculate("%", 1, 0)

    def test_sqrt_negative(self):
        with self.assertRaises(CalculatorError):
            calculate("sqrt", -4)

    def test_power_overflow(self):
        with self.assertRaises(CalculatorError):
            calculate("**", 10.0, 1000)

    def test_zero_to_negative_power(self):
        with self.assertRaises(CalculatorError):
            calculate("**", 0, -1)

    def test_complex_result(self):
        with self.assertRaises(CalculatorError):
            calculate("**", -8, 0.5)

    def test_invalid_operator(self):
        with self.assertRaises(CalculatorError):
            calculate("&", 1, 2)

    def test_missing_second_operand(self):
        with self.assertRaises(CalculatorError):
            calculate("+", 1)

    def test_format_result(self):
        self.assertEqual(format_result(5.0), "5")
        self.assertEqual(format_result(2.5), "2.5")


if __name__ == "__main__":
    unittest.main()
