# A6Q2
# Question: Write a function that takes a string as a parameter and returns a string
#           with every successive repetitive character replaced with a star(*).
#           For example, 'hello' is returned as 'he**o'.
# Name: Satyajeet Nayak
# Appl No: 25C200429

s = input("Enter a string: ")
result = ""
for i in range(len(s)):
    if i > 0 and s[i] == s[i-1]:
        result += '*'
    elif i < len(s)-1 and s[i] == s[i+1]:
        result += '*'
    else:
        result += s[i]
print(result)
