print("\n--- QUIZ SET 1 OUTPUT ---\n")

# Q1
try:
    print("A")
    print(10 / 2)
    print("B")
except:
    print("Error")

# Q2
try:
    print(1)
except:
    print(2)
else:
    print(3)

# Q3
try:
    print(1)
    raise ValueError
    print(2)
except ValueError:
    print(3)
finally:
    print(4)

# Q4
try:
    print("Try")
except:
    print("Except")
else:
    print("Else")
finally:
    print("Finally")

# Q5
try:
    a = int("10.5")
except ValueError:
    print("ValueError")
else:
    print("Success")

# Q6
try:
    print("X")
    1 / 0
except ZeroDivisionError:
    print("Y")
except:
    print("Z")

# Q7
try:
    print(1)
    try:
        print(2 / 0)
    finally:
        print(3)
except:
    print(4)

# Q8
f = open("test.txt", "w")
f.write("Python\n")
f.write("Programming")
f.close()

f = open("test.txt", "r")
print(f.read())
f.close()

# Q9
f = open("a.txt", "w")
f.write("ABC\nDEF")
f.close()

f = open("a.txt", "r")
print(f.readline(), end="")
print(f.readline())
f.close()

# Q10
f = open("x.txt", "w")
f.write("Hello")
f.close()

f = open("x.txt", "r")
f.seek(2)
print(f.read())
f.close()

# Q11
f = open("x.txt", "w")
f.write("Hello")
try:
    print(f.read())
except:
    print("Cannot read in write mode")
f.close()

# Q12
f = open("file.txt", "w")
f.write("A")
f.close()

f = open("file.txt", "a")
f.write("B")
f.close()

f = open("file.txt", "r")
print(f.read())
f.close()

# Q13
f = open("t.txt", "w")
f.write("A\nB\nC")
f.close()

f = open("t.txt", "r")
for line in f:
    print(line, end="")
f.close()

# Q14
f = open("x.txt", "w")
f.write("HelloITER")
f.close()

f = open("x.txt", "r")
f.seek(2)
print(f.read())
f.seek(2)
print(f.read())
print(f.tell())
f.close()

# Q15
f = open("a.txt", "w+")
f.write("ABC")
f.seek(0)
f.write("X")
f.seek(0)
print(f.read())
f.close()

# Q16
f = open("a.txt", "a+")
f.write("Hello")
f.seek(0)
print(f.read())
f.close()

# Q17
f = open("a.txt", "w")
f.write("ABC")
f.close()

f = open("a.txt", "r")
f.seek(10)
print(f.read())
f.close()

# Q18
f = open("a.txt", "w+")
f.write("ABCDE")
print(f.tell())
f.seek(2)
print(f.tell())


# Q19
f = open("a.txt", "w+")
print(f.tell())
f.write("ABC")
print(f.tell())


# Q20
f = open("f3.txt", "w+")
f.write("ABCDE")
f.seek(2)
print(f.read(2))


