# Q7
n = int(input("How many numbers? "))
total = 0
for i in range(n):
    x = float(input("Enter number: "))
    total += 1/x
hm = n / total
print("Harmonic Mean:", hm)
