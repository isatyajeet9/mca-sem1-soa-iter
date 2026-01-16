# A2Q9
# Question: Write a python program that takes two positive integers from command line
#           and prints true if either evenly divides the other.
# Name: Satyajeet Nayak
# Appl No: 25C200429



a = int(input("Enter first num:"))
b = int(input("Enter second num:"))
if a % b == 0 or b % a == 0:
    print(True)
else:
    print(False)
