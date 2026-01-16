# Creating file
f = open("PYTHON", "w")
f.write('"i am great" and ')
f.write('"failure is a part of success"')
f.close()

# Reading file
f = open("PYTHON", "r")
print(f.read())
f.close()
