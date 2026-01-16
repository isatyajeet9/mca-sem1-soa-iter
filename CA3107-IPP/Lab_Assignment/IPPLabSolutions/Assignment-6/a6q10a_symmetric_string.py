s = input("Enter a string: ")
mid = len(s) // 2
if len(s) % 2 == 0:
    if s[:mid] == s[mid:]:
        print("Symmetric")
    else:
        print("Asymmetric")
else:
    if s[:mid] == s[mid+1:]:
        print("Symmetric")
    else:
        print("Asymmetric")
