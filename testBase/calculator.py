## Base on Python 3

class Calculator:
    def __init__(self):
        self.num_1 = None
        self.num_2 = None
        self.operator = None
        self.result = None

    def get_first(self):
        self.num_1 = float(input("Input the first number: "))
        return self.num_1

    def get_second(self):
        self.num_2 = float(input("Input the second number: "))
        return self.num_2

    def get_operator(self):
        self.operator = (input("operator: "))
        return self.operator

    def calculation(self):
        pass


calculator = Calculator()

calculator.get_first()
calculator.get_second()
calculator.get_operator()
