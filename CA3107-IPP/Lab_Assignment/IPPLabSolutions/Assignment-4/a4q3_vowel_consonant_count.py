# A4Q3
# Question: Write a Python program to accept 5 alphabets and count the number of small
#           letters, number of capital letters, count the number of vowels and number of consonants.
# Name: Satyajeet Nayak
# Appl No: 25C200429

small = capital = vowels = consonants = 0
for i in range(5):
    ch = input("Enter alphabet: ")
    if ch.islower():
        small += 1
    if ch.isupper():
        capital += 1
    if ch.lower() in 'aeiou':
        vowels += 1
    else:
        consonants += 1
print("Small letters:", small)
print("Capital letters:", capital)
print("Vowels:", vowels)
print("Consonants:", consonants)
