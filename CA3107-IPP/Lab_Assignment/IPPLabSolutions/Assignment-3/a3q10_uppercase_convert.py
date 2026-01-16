# A3Q10
# Question: Write a function named as 'UpperCase' which converts the lower case alphabet
#           to uppercase alphabet. Also, assert that the entered alphabet by user is valid
#           lowercase alphabet (use ord()). Write a function main that accepts inputs from
#           the user interactively and converts the lowercase alphabet to uppercase using
#           the function 'UpperCase'. (chr() is used to convert ascii value to its
#           corresponding character and ord() returns the ascii value of the given character)
# Name: Satyajeet Nayak
# Appl No: 25C200429
def UpperCase(ch):
    assert 'a' <= ch <= 'z', "Not a lowercase letter"
    return chr(ord(ch) - 32)


ch = input("Enter a lowercase alphabet: ")
print("Uppercase:", UpperCase(ch))

