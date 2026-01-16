# 10. write a recursive function that multiplies two positive numbers and returns the result(use + operator)

def recursiveMul(a, b):
    if b == 0:
        return 0
    if b == 1:
        return a
    return a + recursiveMul(a, b - 1)

print(recursiveMul(5, 3))
