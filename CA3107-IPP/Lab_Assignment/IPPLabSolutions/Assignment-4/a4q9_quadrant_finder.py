# A4Q9
# Question: Write a python program that takes the x-y coordinates of a point in the
#           Cartesian plane and prints a message telling either an axis on which the
#           point lies or the quadrant in which it is found.
# Name: Satyajeet Nayak
# Appl No: 25C200429

x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))

if x == 0 and y == 0:
    print("The point is at the origin.")
elif x == 0:
    print("The point is on the y-axis.")
elif y == 0:
    print("The point is on the x-axis.")
elif x > 0 and y > 0:
    print("The point is in quadrant I.")
elif x < 0 and y > 0:
    print("The point is in quadrant II.")
elif x < 0 and y < 0:
    print("The point is in quadrant III.")
else:
    print("The point is in quadrant IV.")
