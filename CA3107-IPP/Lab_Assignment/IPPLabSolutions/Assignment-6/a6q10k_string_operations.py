s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
count = 0
s2_temp = list(s2)
for ch in s1:
    if ch in s2_temp:
        count += 1
        s2_temp.remove(ch)
print("Common characters:", count)
