# A7Q1
# Question: Write a function that takes a list of values as input parameter and returns
#           another list without any duplicates.
# Name: Satyajeet Nayak
# Appl No: 25C200429

def removeDuplicates(l):
    newList = []
    for item in l:
        if item not in newList:
            newList.append(item)
    return newList

l = [1, 2, 2, 3, 4, 4, 5, 1, 6]
print(removeDuplicates(l))
