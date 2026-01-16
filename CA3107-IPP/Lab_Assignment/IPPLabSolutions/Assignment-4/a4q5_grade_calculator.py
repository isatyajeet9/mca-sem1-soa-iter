# A4Q5
# Question: Write a Python program to assign a grade on the basis of marks obtained by the
#           student using an if-elif-else statement.
#           [90-100]=O, [80-89]=A, [70-79]=B, [60,69]=C, [50,59]=D, [40,49]=E, [<40]=F
# Name: Satyajeet Nayak
# Appl No: 25C200429

marks = int(input("Enter marks: "))
if marks >= 90:
    grade = "O"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
elif marks >= 40:
    grade = "E"
else:
    grade = "F"
print("Grade:", grade)
