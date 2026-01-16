# A6Q8
# Question: Write a function that takes a string as an input and determines the count
#           of the number of words.
# Name: Satyajeet Nayak
# Appl No: 25C200429

def count_words(s):
    words = s.split()
    return len(words)

s = input("Enter a string: ")
print("Number of words:", count_words(s))
