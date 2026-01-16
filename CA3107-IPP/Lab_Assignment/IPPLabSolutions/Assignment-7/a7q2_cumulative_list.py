# A7Q2
# Question: Write a function that takes a list of numbers as input from the user and
#           produces the corresponding cumulative list where each element in the list
#           at index i is the sum of elements at index j <= i.
# Name: Satyajeet Nayak
# Appl No: 25C200429

def create_cumulative_list(numbers):
    cumulative_list = []
    current_sum = 0
    for num in numbers:
        current_sum += num
        cumulative_list.append(current_sum)
    return cumulative_list

numbers = [1, 2, 3, 4, 5]
print(create_cumulative_list(numbers))
