# A4Q11
# Question: Write a python program to calculate electricity bill according to the given
#           conditions. Input the number of units consumed from keyboard.
# Name: Satyajeet Nayak
# Appl No: 25C200429

units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10

print("Electricity Bill: Rs", bill)
