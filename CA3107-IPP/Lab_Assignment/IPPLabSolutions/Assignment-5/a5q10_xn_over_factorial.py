# Q10
x = int(input("Enter x: "))
n = int(input("Enter n: "))
fact = 1
for i in range(1, n+1):
    fact *= i
result = x**n / fact
print("Result:", result)
