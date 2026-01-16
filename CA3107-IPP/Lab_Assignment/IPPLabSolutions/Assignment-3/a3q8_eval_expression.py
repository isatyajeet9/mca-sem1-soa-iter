# A3Q8
# Question: Using a function evaluate the value of the arithmetic expression taken from
#           the user. Hint: Expression will act as an argument while defining function.
# Name: Satyajeet Nayak
# Appl No: 25C200429
def evaluate(exp):
    return eval(exp)

expression = input("Enter an arithmetic expression: ")
print("Result:", evaluate(expression))
