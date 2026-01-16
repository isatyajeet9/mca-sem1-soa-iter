# Q18
x = float(input("Enter x: "))
n = int(input("Enter n: "))
s = 0
sign = 1
for i in range(1, 2*n, 2):
    fact = 1
    for j in range(1, i+1):
        fact *= j
    s += sign * x**i / fact
    sign *= -1
print("Sum:", s)
