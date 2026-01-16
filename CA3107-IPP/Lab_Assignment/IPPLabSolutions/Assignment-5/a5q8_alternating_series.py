# Q8
n = int(input("Enter n: "))
s = 0
sign = 1
for i in range(1, 2*n, 2):
    s += sign * i
    sign *= -1
print("Sum S:", s)
