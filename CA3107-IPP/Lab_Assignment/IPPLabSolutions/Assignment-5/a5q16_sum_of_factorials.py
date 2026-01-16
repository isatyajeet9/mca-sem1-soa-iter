# Q16
n = int(input("Enter n: "))
sum_fs = 0
for i in range(n+1):
    fact = 1
    for j in range(1, i+1):
        fact *= j
    sum_fs += fact
print("Sum:", sum_fs)
