# A6Q7
# Question: Write a function that takes a sentence as an input parameter and replaces
#           the first letter of every word with the corresponding uppercase letter and
#           rest of the letters in the word by corresponding letters in lowercase
#           without using built-in function.
# Name: Satyajeet Nayak
# Appl No: 25C200429
sentence = "ViRat HITS a CENTURY in THE match"
words = sentence.split()
rv = ""
for word in words:
    rv += word[0].upper() + word[1:].lower() + " "
print(rv.strip()) 
