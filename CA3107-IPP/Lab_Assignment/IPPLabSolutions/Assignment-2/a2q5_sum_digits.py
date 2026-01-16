# A2Q5
# Question: Write a python program that reads an integer between 100 and 999 and adds
#           all the digits in the integer. For example, if an integer is 672, the sum
#           of all its digits is 15.
# Name: Satyajeet Nayak
# Appl No: 25C200429


num = int(input("Enter an integer between 100 and 999: "))

hundreds_digit = num // 100
tens_digit = (num // 10) % 10
units_digit = num % 10

digit_sum = hundreds_digit + tens_digit + units_digit

print(f"Sum of digits: {digit_sum}")
