# A3Q11
# Name: Satyajeet Nayak
def swap(a,b):
    a,b = b,a
    return a,b

x,y = 5,10
print("Before swap:", x, y)
x,y = swap(x,y)
print("After swap:", x, y)
