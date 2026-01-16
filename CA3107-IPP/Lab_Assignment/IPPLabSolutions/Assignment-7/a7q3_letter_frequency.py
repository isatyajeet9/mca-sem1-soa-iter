# A7Q3
# Question: Write a program that takes a sentence as input from the user and computes
#           the frequency of each letter. Use a variable of dictionary type to maintain the count.
# Name: Satyajeet Nayak
# Appl No: 25C200429

sentence = input("Enter a sentence: ")
frequency_dict = {}

for char in sentence:
    if char.isalpha():
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1

print(frequency_dict)
