# A6Q5
# Question: Write a function that takes two strings and returns True if they are anagrams
#           and False otherwise. A pair of strings is anagrams if the letters in one word
#           can be arranged to form the second one.
# Name: Satyajeet Nayak
# Appl No: 25C200429
str1 = "teacher"
str2 = "cheater"
if sorted(str1) == sorted(str2):
    print(True) 
else:
    print(False)
