# Q14.
n = int(input("Enter a positive integer: "))
binary = ""
while n > 0:
    binary = str(n % 2) + binary
    n //= 2
print("Binary:", binary)