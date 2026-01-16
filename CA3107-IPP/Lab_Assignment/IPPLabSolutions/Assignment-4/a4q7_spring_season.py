# A4Q7
# Question: Write a python program that takes two integer values m and d and prints true
#           if day d of month m is between 3/20 and 6/20, false otherwise.
# Name: Satyajeet Nayak
# Appl No: 25C200429

m = int(input("Enter month (1-12): "))
d = int(input("Enter day (1-31): "))

if (m == 3 and d >= 20) or (m in [4, 5]) or (m == 6 and d <= 20):
    print(True)
else:
    print(False)
