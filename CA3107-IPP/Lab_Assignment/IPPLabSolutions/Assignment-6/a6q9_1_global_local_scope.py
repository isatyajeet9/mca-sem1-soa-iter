# A6Q9 (Part 1)
# Question: Study the program segments given below. Give the output produced, if any.
#           (Testing global and local variable scope)
# Name: Satyajeet Nayak
# Appl No: 25C200429

globalVar = 10
def test():
    localVar = 20
    print('Inside function test :globalVar =', globalVar)
    print('Inside function test : localVar=', localVar)
test()
print('Outside function test : globalVar=', globalVar)
print('Outside function test : localVar=', localVar)