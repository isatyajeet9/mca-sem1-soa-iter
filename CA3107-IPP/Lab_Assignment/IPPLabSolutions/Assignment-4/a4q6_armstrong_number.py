# A4Q6
# Question: Write a program that checks whether a given 3 digit number is an Armstrong
#           number or not. A 3 digit number is an Armstrong number whose sum of the cubes
#           of the digits is equal to the number itself. For Example, 370 = 3^3 + 7^3 + 0^3
# Name: Satyajeet Nayak
# Appl No: 25C200429

num = int(input("Enter a 3-digit number: "))
arm = 0
temp = num
while temp > 0:
    rem = temp % 10
    arm = arm + (rem ** 3)
    temp //= 10
if num == arm:
    print("Yes, it is an Armstrong number")
else:
    print("No, it is not an Armstrong number")
