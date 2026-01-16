# A4Q12
# Question: Write a python program to check whether the input 3 digit number is a
#           perfect number or not.
# Name: Satyajeet Nayak
# Appl No: 25C200429

num = int(input("Enter a 3-digit number: "))
sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i

if sum == num:
    print("It is a perfect number.")
else:
    print("It is not a perfect number.")
