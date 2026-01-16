# 13. write a recursive function to find the length of a string

def recursiveLen(s):
    if s == "":
        return 0
    return 1 + recursiveLen(s[1:])

s1 = "Virat Kohli"
print(recursiveLen(s1))
