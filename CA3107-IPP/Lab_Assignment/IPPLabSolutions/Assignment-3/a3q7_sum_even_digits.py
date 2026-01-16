# A3Q7
# Question: Define a function to find the sum of even digits of a four-digit number
#           without using control structures.
# Name: Satyajeet Nayak
# Appl No: 25C200429


def sumEvenDigits(num):

    d1 = num // 1000
    d2 = (num // 100) % 10
    d3 = (num // 10) % 10
    d4 = num % 10

    total = ((d1 * (1 - d1 % 2)) + (d2 * (1 - d2 % 2)) + (d3 * (1 - d3 % 2)) + (d4 * (1 - d4 % 2)))

    return total


number = int(input("Enter a four-digit number: "))
print("Sum of even digits:", sumEvenDigits(number))
