# A2Q10
# Question: Write a Python program to calculate the root of the given quadratic equation
#           ax² + bx + c = 0 for different values of a, b, c. If the discriminant is
#           greater than zero it should print 2 real roots, if it is equal to 0 it should
#           print 1 root and if it is less than zero it should print the message that
#           there is no real roots for the given equation.
# Name: Satyajeet Nayak
# Appl No: 25C200429


a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
discriminant = b**2 - 4 * a * c
if discriminant > 0:
    print("Two real roots:")
elif discriminant == 0:
    print(
        "One real root:",
    )
else:
    print("No real roots for the given equation.")
