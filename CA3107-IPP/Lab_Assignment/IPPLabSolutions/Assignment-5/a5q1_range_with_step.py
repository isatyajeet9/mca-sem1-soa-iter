# A5Q1
# Question: Write a program that gets three integers from the user. Count from the first
#           number to the second number in increments of the third number.
# Name: Satyajeet Nayak
# Appl No: 25C200429

start = int(input("from: "))
end = int(input("to: "))
step = int(input("step by: "))
for i in range(start, end, step):
    print(i, end=" ")
print()
