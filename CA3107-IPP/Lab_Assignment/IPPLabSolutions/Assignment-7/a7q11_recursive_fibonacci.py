# 11. write a recursive function to find nth Fibonacci number

def fibonacci(n):
    if n <= 0:
        return "Input must be positive integer"
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

n = 7
print(fibonacci(n))
