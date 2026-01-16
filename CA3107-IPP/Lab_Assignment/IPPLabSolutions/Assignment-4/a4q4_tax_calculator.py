# A4Q4
# Question: Write a Python program to calculate tax using an if-elif-else statement.
#           Cost > 100000: 15%, Cost > 50000 and <= 100000: 10%, Cost <= 50000: 5%
# Name: Satyajeet Nayak
# Appl No: 25C200429

cost = int(input("Enter cost in Rs: "))
if cost > 100000:
    tax = cost * 0.15
elif cost > 50000:
    tax = cost * 0.10
else:
    tax = cost * 0.05
print("Tax to be paid:", tax)
