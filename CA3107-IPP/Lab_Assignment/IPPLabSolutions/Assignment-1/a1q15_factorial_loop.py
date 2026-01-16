# A1Q15
# Question: Assume a string variable str1 contains "1" initially i.e. str1="1"
#           Write a python program to print the following output using string concatenation.
#           1
#           1 2 1
#           1 2 1 3 1 2 1
#           1 2 1 3 1 2 1 4 1 2 1 3 1 2 1
# Name: Satyajeet Nayak
# Appl No: 25C200429

result = 1
for i in range(1, 4):
    result *= i
print(result) 
