# A2Q3
# Question: WAP to input principal, rate, time and calculate Simple Interest.
#           Simple Interest=Principal*Rate*Time/100
# Name: Satyajeet Nayak
# Appl No: 25C200429


P = float(input("Enter Principal:"))
R = float(input("Enter Rate of Interest:"))
T = float(input("Enter Time: (year)"))

SI = (P * R * T) / 100
print("Simple Interest:", SI)
