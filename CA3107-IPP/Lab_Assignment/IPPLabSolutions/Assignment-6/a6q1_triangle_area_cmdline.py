# A6Q1
# Question: Write a function areatriangle() that takes 3 sides as commandline arguments
#           and calculate the area of the triangle.
# Name: Satyajeet Nayak
# Appl No: 25C200429

# 1
import math
import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
s = (a + b + c) / 2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area:", area) 