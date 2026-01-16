# A6Q6
# Question: Write a function that takes a sentence as an input parameter and displays
#           the number of words starting with a vowel in the sentence.
# Name: Satyajeet Nayak
# Appl No: 25C200429
sentence = "Virat hits a century in the match"
vowels = "aeiouAEIOU"
count = 0
for word in sentence.split():
    if word[0] in vowels:
        count += 1
print(count)
