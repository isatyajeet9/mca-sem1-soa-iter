# A7Q4
# Question: Identify the output produced when the following functions are invoked.
#           (Two list creation and swap functions)
# Name: Satyajeet Nayak
# Appl No: 25C200429

print("--- Case 1 ---")
def func():
    l1 = list()
    l2 = list()
    for i in range(0,5):
        l1.append(i)
        l2.append(i+3)
    print(l1)
    print(l2)
func()

print("\n--- Case 2 ---")
def func():
    l1 = list()
    l2 = list()
    for i in range(0,5):
        l1.append(i)
        l2.append(i+3)
    l1, l2 = l2, l1
    print(l1)
    print(l2)
func()
