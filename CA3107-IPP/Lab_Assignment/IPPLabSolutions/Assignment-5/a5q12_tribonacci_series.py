# Q12
n = int(input("Enter number of terms: "))
a, b, c = 1, 2, 3
print(a, b, c, end=" ")
for i in range(3, n):
    d = a + b + c
    print(d, end=" ")
    a, b, c = b, c, d

