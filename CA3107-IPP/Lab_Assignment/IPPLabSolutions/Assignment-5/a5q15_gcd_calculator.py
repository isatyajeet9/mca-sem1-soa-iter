# Q15
x = int(input("Enter x: "))
y = int(input("Enter y: "))
while y != 0:
    x, y = y, x % y
print("GCD:", x)
