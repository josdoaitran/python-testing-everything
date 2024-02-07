import unittest
from python_testing4everyone_tutorial.apps.practice_math_operator.tax_calculator import TaxCalculator
class TestTaxCalculator(unittest.TestCase):

    def test_tax_calculation(self):
        # Test case 1: Basic calculation
        result = TaxCalculator.tax(100, 10)
        self.assertEqual(result, 90)

        # Test case 2: Zero tax
        result = TaxCalculator.tax(200, 0)
        self.assertEqual(result, 200)

        # Test case 3: Maximum tax
        result = TaxCalculator.tax(500, 100)
        self.assertEqual(result, 0)

        # Test case 4: Negative tax
        result = TaxCalculator.tax(300, -20)
        self.assertEqual(result, 360)

        # Test case 5: Decimal tax
        result = TaxCalculator.tax(150, 7.5)
        self.assertEqual(result, 138)


if __name__ == '__main__':
    unittest.main()