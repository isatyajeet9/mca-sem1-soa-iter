# 14. write a recursive function to reverse a string

def recursiveReverse(s):
    if len(s) == 0:
        return s
    return s[-1] + recursiveReverse(s[:-1])

s = "Hello World"
print(recursiveReverse(s))
