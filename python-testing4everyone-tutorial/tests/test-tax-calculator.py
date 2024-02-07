import unittest

from test-base import calculator
from python-testing4everyone- import tax


class TestTaxCalculator(unittest.TestCase):

    def test_tax_calculation(self):
        # Test case 1: Basic calculation
        result = tax(100, 10)
        self.assertEqual(result, 90)

        # Test case 2: Zero tax
        result = tax(200, 0)
        self.assertEqual(result, 200)

        # Test case 3: Maximum tax
        result = tax(500, 100)
        self.assertEqual(result, 0)

        # Test case 4: Negative tax
        result = tax(300, -20)
        self.assertEqual(result, 360)

        # Test case 5: Decimal tax
        result = tax(150, 7.5)
        self.assertEqual(result, 138)


if __name__ == '__main__':
    unittest.main()