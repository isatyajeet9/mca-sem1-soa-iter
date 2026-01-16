# A8Q3
# Question: Write a Python function that takes data to be stored in the file 'file1'
#           as interactive input from the user until he responds with nothing as input.
#           Each line taken as input should be capitalized, and stored in the file.
# Name: Satyajeet Nayak
# Appl No: 25C200429

f = open("file1.txt", "w")

while True:
    s = input("Enter text: ")
    if s == "":
        break
    f.write(s.upper() + "\n")

f.close()

f = open("file1.txt", "r")
print(f.read())
f.close()
