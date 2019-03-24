
class calculator:
    def __init__(self):
        self.num_1 = None
        self.num_2 = None
        self.operator = None
        self.result = None

    def get_first(self):
        self.num_1 = float(input("Input the first number: "))
        return self.num_1

    def get_second(self):
        self.num_2 = float(input("Input the second number: "))
        return self.num_2

    def get_operator(self):
        self.operator = float(input("Input the operation: "))
        return self.operator

    def calculation(self):
        pass


calculation = Calculation()

calculation.get_first()
calculation.get_second()
calculation.get_operator()
