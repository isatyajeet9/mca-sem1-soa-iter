print("\n--- QUIZ SET 2 OUTPUT ---\n")

# Q1
f = open("f5.txt", "a+")
f.write("Hi")
f.seek(0)
print(f.read())
f.close()

# Q2
f = open("f6.txt", "w+")
print(f.tell())
f.write("XYZ")
print(f.tell())
f.close()

# Q3
f = open("f9.txt", "w")
f.write("A\nB\nC")
f.close()

# Q4
f = open("f9.txt", "r")
for line in f:
    print(line, end="")
f.close()

# Q5
f = open("f10.txt", "w+")
f.write("12345")
f.seek(1)
f.write("X")
f.seek(0)
print(f.read())
f.close()

# Q6
try:
    print("Start")
    raise ValueError
except:
    print("Except")
else:
    print("Else")
finally:
    print("Finally")

# Q7
def fun():
    try:
        return 10
    finally:
        return 20
print(fun())

# Q8
try:
    print("A")
    1 / 0
except:
    print("B")
    raise
finally:
    print("C")

# Q9
try:
    pass
finally:
    print("Hello")

# Q10
try:
    print("A")
    print(1 / 0)
    print("B")
except ZeroDivisionError:
    print("C")
finally:
    print("D")

# Q11
try:
    x = int("10")
except ValueError:
    print("Error")
else:
    print(x)

# Q12
try:
    print(1)
    try:
        print(2 / 0)
    except ValueError:
        print(3)
    finally:
        print(4)
except:
    print(5)

# Q13
try:
    raise KeyError
except IndexError:
    print("Index")
except:
    print("Other")

# Q14
def test():
    try:
        return "Try"
    except:
        return "Except"
    finally:
        print("Finally")
print(test())

# Q15
try:
    print(10)
except:
    print(20)
else:
    print(30)
finally:
    print(40)

# Q16
try:
    print("X")
    raise ValueError
except ValueError:
    print("Y")
finally:
    print("Z")

# Q17
try:
    print("Hello")
    raise Exception
except:
    print("Except")
    raise
finally:
    print("Finally")

# Q18
try:
    f = open("a.txt", "r")
    print(f.read())
except:
    print("FileError")

# Q19
try:
    f = open("b.txt", "w")
    f.write("Python")
    print(f.read())
except:
    print("Error")
finally:
    print("Done")

# Q20
try:
    f = open("c.txt", "w+")
    f.write("ABC")
    print(f.read())
except:
    print("Error")