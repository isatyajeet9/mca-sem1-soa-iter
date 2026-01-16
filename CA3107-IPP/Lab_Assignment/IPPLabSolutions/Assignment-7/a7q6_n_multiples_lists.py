# A7Q6
# Question: Write a function that takes n as an input and creates a list of n lists
#           such that ith list contains first five multiples of i.
# Name: Satyajeet Nayak
# Appl No: 25C200429

def createNLists(n):
    result_list = []
    for i in range(n):
        multiples = [i * j for j in range(1, 6)]
        result_list.append(multiples)
    return result_list

n = 5
print(createNLists(n))
