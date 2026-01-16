s = input("Enter a string: ")
has_digit = False
has_alpha = False
for ch in s:
    if ch.isdigit():
        has_digit = True
    elif ch.isalpha():
        has_alpha = True
if has_digit and has_alpha:
    print("Yes")
else:
    print("No")
