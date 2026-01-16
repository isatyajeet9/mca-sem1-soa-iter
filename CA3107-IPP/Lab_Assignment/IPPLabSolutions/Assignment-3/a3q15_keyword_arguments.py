# A3Q15
# Name: Satyajeet Nayak
def fun(a=0,b=1):
    return (a**2 + b**2)

print("a:", fun(2,a=3))
print("b:", fun(b=3,2)) # invalid syntax
print("c:", fun(3,b=2))
print("d:", fun(a=4,5))  # valid: 4**2 + 5**2
