import unittest
from python_testing4everyone_tutorial.apps.example_method.calculate_net_price import NetPrice

class TestCasesCalculateNetPrice(unittest.TestCase):

    # Given the sales price and sale tax, write a function to calculate the net price of an item.
    # Price value: 10 - 100
    # Tax: No more than 20 %
    # For example, if the sale price is $120 and the sale tax is 20 %, the output should be $96.

    def testcase_calculate(self):
        ## Step 1
        # print (NetPrice.calculate(10, 0.1))
        # print(NetPrice.calculate(100, 0.1))
        # print(NetPrice.calculate(11, 0.2))
        # print(NetPrice.calculate(9, 0.1))

        ## Step 2
        ## Input assert to verify all passed

        # self.assertEqual(NetPrice.calculate(10, 0.1), 0.9)
        # self.assertEqual(NetPrice.calculate(100, 0.1), 0.9)
        # self.assertEqual(NetPrice.calculate(11, 0.2), 0.9)
        # self.assertEqual(NetPrice.calculate(9, 0.1), 0.9)

        ## Step 3
        ## Input assert to verify and 1 fauled test case

        # self.assertEqual(NetPrice.calculate(10, 0.1), 0.9)
        # self.assertEqual(NetPrice.calculate(100, 0.1), 0.9)
        # self.assertEqual(NetPrice.calculate(11, 0.2), 0.9)
        # self.assertEqual(NetPrice.calculate(9, 0.1), 0.8)

        ## Step 4, Adjust the proper value of expected fields

        self.assertEqual(NetPrice.calculate(10, 0.1), 9)
        self.assertEqual(NetPrice.calculate(100, 0.1), 90)
        self.assertEqual(NetPrice.calculate(11, 0.2), 8.8)
        self.assertEqual(NetPrice.calculate(9, 0.1), 8.1)
        self.assertEqual(NetPrice.calculate(101, 0.1), "Input price less than 100")