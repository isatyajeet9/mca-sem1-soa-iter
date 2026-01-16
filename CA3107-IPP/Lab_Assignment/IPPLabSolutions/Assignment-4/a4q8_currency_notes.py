# A4Q8
# Question: Write a program to print the number of 20 rupee notes, 10 rupee notes, 5 rupee
#           and 1 rupee notes a person has if the total amount of money with that person
#           is given (assuming that only the given denominations are there with the person).
# Name: Satyajeet Nayak
# Appl No: 25C200429

amount = int(input("Enter total amount: "))

n20 = amount // 20
amount %= 20
n10 = amount // 10
amount %= 10
n5 = amount // 5
n1 = amount % 5

print("20 Rs notes:", n20)
print("10 Rs notes:", n10)
print("5 Rs notes:", n5)
print("1 Rs notes:", n1)
