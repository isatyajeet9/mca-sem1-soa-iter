# A4Q1
# Question: Write a Python program to check whether a year is leap year or not.
# Name: Satyajeet Nayak
# Appl No: 25C200429

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")