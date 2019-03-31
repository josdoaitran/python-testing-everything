## Base on Python 3
import os , time

class Calculator:
    def __init__(self):
        self.num_1 = None
        self.num_2 = None
        self.operator = None
        self.result = None

    def get_first(self):
        try:
            self.num_1 = float(input("Input the first number: "))
        except:
            print("Wrong input !!! Please try againn \n")
            self.get_first()
        finally:
            self.get_operator()

        #return self.num_1

    def get_second(self):
        try:
            self.num_2 = float(input("Input the second number: "))
        except:
            print("Wrong input !!! Please try again")
            self.get_second()
        finally:
            self.calculation()
        #return self.num_2

    def get_operator(self):
        self.operator = (input("operator: "))
        if self.operator == '+' or self.get_operator == '-' or self.operator == '%' or self.operator == '/' or self.operator == '*':
            self.get_second()
        else:
            print("Wrong input !!! Please try again \n")
            self.get_operator()
        #return self.operator

    def calculation(self):
        if self.operator == '+':
            self.result = self.num_1 + self.num_2
        if self.operator == '-':
            self.result = self.num_1 - self.num_2
        if self.operator == '/':
            self.result = self.num_1 / self.num_2
        if self.operator == '%':
            self.result = self.num_1 % self.num_2
        if self.operator == '*':
            self.result = self.num_1 * self.num_2
        return self.result


calculator = Calculator()
running = True

while running:
    os.system('clear')
    calculator.get_first()
    print(calculator.result)

    more = input("Press any key to continue or Q to quite: \n")
    if more == "q".upper():
        print("Terminate")
        time.sleep(1)
        running = False
    else:
        continue
