# Exercise 2: Examining Differences Between Files

class Compute:
    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands

    def multiply(self):
        if self.operands is None:
            return
        product = 1
        for item in self.operands:
            product *= item
        print(product)

    def subtract(self):
        pass

    def divide(self):
        pass

    def multiply(self):
        sum  = 1
        for item in self.operands:
            sum *= item
        print(sum)

