# A3Q12
# Name: Satyajeet Nayak
import math
def areaTriangle(a,b,c):
    assert a+b>c and b+c>a and c+a>b, "Invalid sides"
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area

def main():
    a = float(input("Enter side1: "))
    b = float(input("Enter side2: "))
    c = float(input("Enter side3: "))
    print("Area of triangle:", areaTriangle(a,b,c))

main()
