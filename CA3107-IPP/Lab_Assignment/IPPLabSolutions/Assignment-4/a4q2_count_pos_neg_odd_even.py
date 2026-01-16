# A4Q2
# Question: Write a Python program to accept 5 numbers. Count the number of positive
#           numbers, number of negative numbers, number of odd numbers and number of even numbers.
# Name: Satyajeet Nayak
# Appl No: 25C200429

pos = 0
neg = 0
odd = 0
even = 0

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))


    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1

    if num % 2 == 0:
        even += 1
    else:
        odd += 1


print(f"Number of positive numbers: {pos}")
print(f"Number of negative numbers: {neg}")
print(f"Number of even numbers: {even}")
print(f"Number of odd numbers: {odd}")