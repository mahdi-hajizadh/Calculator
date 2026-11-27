import unittest

from arithmetic import calculate_expression


class ArithmeticTests(unittest.TestCase):
    def test_precedence_and_grouping(self):
        self.assertEqual(calculate_expression(" 2 + (-3 * 4) / 2 "), -4)
        self.assertEqual(calculate_expression("0.5 + +1.5"), 2)

    def test_rejects_unsupported_and_non_finite_input(self):
        for expression in ("answer", "abs(1)", "1e999", "9" * 257):
            with self.subTest(expression=expression), self.assertRaises(ValueError):
                calculate_expression(expression)

    def test_reports_invalid_math_and_syntax(self):
        with self.assertRaises(ZeroDivisionError):
            calculate_expression("5 / 0")
        with self.assertRaises(SyntaxError):
            calculate_expression("3 +")
