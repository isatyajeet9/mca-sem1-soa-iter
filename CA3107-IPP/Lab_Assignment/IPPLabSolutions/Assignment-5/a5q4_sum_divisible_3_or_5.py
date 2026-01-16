# Q4
N = int(input("Enter N: "))
total = 0
for i in range(N):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print("Sum:", total)
