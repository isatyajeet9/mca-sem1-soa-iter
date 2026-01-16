# A8Q10
# Question: What will be the output for the following code snippets if the file being
#           opened does not exist?
# Name: Satyajeet Nayak
# Appl No: 25C200429

try:
    f = open("filejh1.txt", "r")
except IOError:
    print("Problem with Input Output...\n")
else:
    print("No Problem with Input Output...")