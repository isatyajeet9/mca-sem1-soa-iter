# A9Q1
# Question: Create a class to perform arithmetic operations like addition, subtraction,
#           multiplication and division. The attributes of the class are number1 and number2.
# Name: Satyajeet Nayak
# Appl No: 25C200429

class Arithmetic:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def add(self):
        return self.n1 + self.n2

    def sub(self):
        return self.n1 - self.n2

    def mul(self):
        return self.n1 * self.n2

    def div(self):
        return self.n1 / self.n2

obj = Arithmetic(15, 5)

print("Addition =", obj.add())
print("Subtraction =", obj.sub())
print("Multiplication =", obj.mul())
print("Division =", obj.div())
