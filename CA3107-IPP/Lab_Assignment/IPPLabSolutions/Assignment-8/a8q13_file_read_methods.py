#a) 
f = open("PYTHON", "w")
f.write("failure is a part of success")
f.close()

f = open("PYTHON", "r")
print(f.read(4))
f.close()


#b) 
f = open("PYTHON", "w")
f.write("failure is a part of success")
f.close()

f = open("PYTHON", "r")
print(f.read())
f.close()