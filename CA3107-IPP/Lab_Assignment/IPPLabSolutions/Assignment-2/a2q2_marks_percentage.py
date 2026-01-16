# A2Q2
# Question: WAP to Input 5 subject marks of a student and find total marks and
#           percentage obtained by the student.
# Name: Satyajeet Nayak
# Appl No: 25C200429


sub1 = int(input("Enter marks:"))
sub2 = int(input("Enter marks:"))
sub3 = int(input("Enter marks:"))
sub4 = int(input("Enter marks:"))
sub5 = int(input("Enter marks:"))
tm = sub1 + sub2 + sub3 + sub4 + sub5
per = tm / 5
print("Total marks of the student:", tm)
print("Percentage obtained by the student:", per)
