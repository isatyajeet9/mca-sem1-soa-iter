# A4Q13
# Question: Write a python program which displays an appropriate name for a person, using
#           a combination of nested ifs and compound conditions. Ask the user for a gender,
#           first name, last name and age. Display appropriate salutation (Mrs./Ms./Mr.)
#           based on gender, age, and marital status for females.
# Name: Satyajeet Nayak
# Appl No: 25C200429

gender = input("Enter gender (M/F): ")
fname = input("Enter first name: ")
lname = input("Enter last name: ")
age = int(input("Enter age: "))

if gender == 'F' or gender == 'f':
    if age >= 20:
        married = input("Are you married (y/n)? ")
        if married == 'y' or married == 'Y':
            print("Then I shall call you Mrs.", fname, lname)
        else:
            print("Then I shall call you Ms.", fname, lname)
    else:
        print("Then I shall call you", fname, lname)
else:
    if age >= 20:
        print("Then I shall call you Mr.", fname, lname)
    else:
        print("Then I shall call you", fname, lname)
