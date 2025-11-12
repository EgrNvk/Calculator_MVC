class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def addition(self):
        result = self.number1 + self.number2
        return result

    def subtraction(self):
        result = self.number1 - self.number2
        return result

    def multiplication(self):
        result = self.number1 * self.number2
        return result

    def division(self):
        result = self.number1 / self.number2
        return result