# A2Q4
# Question: Body Mass Index (BMI) is a measure of health on weight. It can be calculated
#           by taking your weight in kilograms and dividing by the square of your height
#           in meters. Write a python program that prompts the user to enter a weight in
#           pounds and height in inches and displays the BMI.
#           Note: 1 pound = 0.45359237 kg, 1 inch = 0.0254 meters.
# Name: Satyajeet Nayak
# Appl No: 25C200429


weight_p = float(input("Enter weight in pounds:"))
height_i = float(input("Enter weight in pounds:"))

weight_kg = weight_p * 0.45359237
height_m = height_i * 0.0254

BMI = weight_kg / (height_m**2)

print("BMI is:", BMI)
