# A4Q10
# Question: Write a python program that prompts the user to enter an integer for today's
#           day of the week (Sunday is 0, Monday is 1... and Saturday is 6). Also prompt
#           the user to enter the number of days after today for a future day and display
#           the future day of the week.
# Name: Satyajeet Nayak
# Appl No: 25C200429

today = int(input("Enter today's day: "))
after = int(input("Enter the number of days elapsed since today: "))

future = (today + after) % 7

if today == 0:
    t = "Sunday"
elif today == 1:
    t = "Monday"
elif today == 2:
    t = "Tuesday"
elif today == 3:
    t = "Wednesday"
elif today == 4:
    t = "Thursday"
elif today == 5:
    t = "Friday"
else:
    t = "Saturday"

if future == 0:
    f = "Sunday"
elif future == 1:
    f = "Monday"
elif future == 2:
    f = "Tuesday"
elif future == 3:
    f = "Wednesday"
elif future == 4:
    f = "Thursday"
elif future == 5:
    f = "Friday"
else:
    f = "Saturday"

print("Today is", t, "and the future day is", f)
