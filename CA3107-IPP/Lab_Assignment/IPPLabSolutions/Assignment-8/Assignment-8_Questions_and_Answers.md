# Assignment-8 Questions and Answers

## Q1
**Question:** Write a Python function that takes two file names, datafile1 and datafile2 as input. The function should read the contents of the file datafile1 line by line and should write them to another file datafile2 after adding a newline at the end of each line.

**Code (`a8q1_file_copy.py`):**
```python
# A8Q1
# Question: Write a Python function that takes two file names, datafile1 and datafile2 as
#           input. The function should read the contents of the file datafile1 line by line
#           and should write them to another file datafile2 after adding a newline at the
#           end of each line.
# Name: Satyajeet Nayak
# Appl No: 25C200429

def filecopy(fl1,fl2):
    f1=open(fl1,'w')
    f1.write("My name is Satyajeet\n")
    f1.write("My branch is MCA")
    f1=open(fl1,'r')
    f2=open(fl2,'w')
    print("content of file1")
    for l in f1:
        print(l)
        f2.write(l)

    print("\ncontent of file2")
    f2=open(fl2)
    for l in f2:
        print(l)
    f1.close()
    f2.close()
filecopy('file1','file2')
```

## Q2
**Question:** Write a Python function that reads a file file1 and displays the number of words and the number of vowels in the file.

**Code (`a8q2_word_vowel_count.py`):**
```python
# A8Q2
# Question: Write a Python function that reads a file file1 and displays the number
#           of words and the number of vowels in the file.
# Name: Satyajeet Nayak
# Appl No: 25C200429

def filecount(fl1):
    f1=open(fl1,'w')
    f1.write("My  name is Satyajeet")
    f1.write("My branch is MCA")
    c=0
    cv=0
    f1=open(fl1,'r')
    l=f1.readlines()
    for line in l:
        c+=len(line.split())
        for ch in line:
            if ch.isalpha() and ch in 'aeiouAEIOU':
                cv+=1

            
    print("count of words:",c," ","count of vowels:",cv)
    f1.close()
filecount('file1')
```

## Q3
**Question:** Write a Python function that takes data to be stored in the file 'file1' as interactive input from the user until he responds with nothing as input. Each line taken as input should be capitalized, and stored in the file.

**Code (`a8q3_write_uppercase.py`):**
```python
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
```

## Q4
**Question:** Write a Python function that reads the file file1 and copies only alternative lines to another file file2. Alternative lines copied should be the odd numbered lines.

**Code (`a8q4_alternate_chars.py`):**
```python
# A8Q4
# Question: Write a Python function that reads the file file1 and copies only alternative
#           lines to another file file2. Alternative lines copied should be the odd numbered lines.
# Name: Satyajeet Nayak
# Appl No: 25C200429

def filecopy(fl1,fl2):
    f1=open(fl1,'w')
    f1.write("My  name is Satyajeet")
    f1.write("My branch is MCA")
    f1.write("My section is b2")
    f1=open(fl1,'r')
    print("content of file1")
    l=f1.readline()
    print(l)
    f2=open(fl2,'w')
    for i in range(0,len(l),2):
        f2.write(l[i])
    print("\nContent of file2")
    f2=open(fl2)
    for l in f2:
        print(l)
    f1.close()
    f2.close()
filecopy('file1','file2')
```

## Q5
**Question:** What will be the output produced on executing function inverse1 when the following input is entered as the value of variable num: (a)5 (b)0 (c)2.0 (d)x (e)None

**Code (`a8q5_exception_inverse.py`):**
```python
# A8Q5
# Question: What will be the output produced on executing function inverse1 when the
#           following input is entered as the value of variable num:
#           (a)5 (b)0 (c)2.0 (d)x (e)None
# Name: Satyajeet Nayak
# Appl No: 25C200429

try:
    num = input("Enter the number: ")
    num = float(num)
    inverse = 1.0 / num

except ValueError:
    print("ValueError")
except TypeError:
    print("TypeError")
except ZeroDivisionError:
    print("ZeroDivisionError")
except:
    print("Any other Error")
else:
    print(inverse)
finally:
    print("Function inverse completed")
```

## Q6
**Question:** Examine the function percentage: Determine the output for the following function calls: (a) percentage(150.0, 200.0) (b) percentage(150.0, 0.0) (c) percentage('150.0', '200.0')

**Code (`a8q6_exception_percentage.py`):**
```python
# A8Q6
# Question: Examine the function percentage: Determine the output for the following
#           function calls: (a) percentage(150.0, 200.0) (b) percentage(150.0, 0.0)
#           (c) percentage('150.0', '200.0')
# Name: Satyajeet Nayak
# Appl No: 25C200429

def percentage(marks, total):
    try:
        percent = (marks / total) * 100

    except ValueError:
        print("ValueError")
    except TypeError:
        print("TypeError")
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except:
        print("Any other Error")
    else:
        print(percent)
    finally:
        print("Function percentage completed")


# Test calls:
percentage(150.0, 200.0)
percentage(150.0, 0.0)
percentage("150.0", "200.0")
```

## Q9
**Question:** Identify two exceptions that may be raised while executing the following statement: result = a + b

**Code (`a8q9_expression_result.py`):**
```python
# A8Q9
# Question: Identify two exceptions that may be raised while executing the following
#           statement: result = a + b
# Name: Satyajeet Nayak
# Appl No: 25C200429

result = a + b
```

## Q10
**Question:** What will be the output for the following code snippets if the file being opened does not exist?

**Code (`a8q10_ioerror_handling.py`):**
```python
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
```

## Q11 (File Read/Write)
**Question:** Demonstrate creating a file and reading from it.

**Code (`a8q11_file_read_write.py`):**
```python
# Creating file
f = open("PYTHON", "w")
f.write('"i am great" and ')
f.write('"failure is a part of success"')
f.close()

# Reading file
f = open("PYTHON", "r")
print(f.read())
f.close()
```

## Q12 (Write Error)
**Question:** Demonstrate an error when writing to a file opened in read mode.

**Code (`a8q12_write_error_demo.py`):**
```python
f = open("file1", "r")
f.write('"work is worship"')   # ERROR because file opened in read-mode
f.close()
```

## Q13 (Read Methods)
**Question:** Demonstrate reading specific characters vs reading all content from a file.

**Code (`a8q13_file_read_methods.py`):**
```python
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
```

## Q14 (Readline)
**Question:** Demonstrate reading a single line from a file.

**Code (`a8q14_readline_demo.py`):**
```python

f = open("PYTHON", "w")
f.write("failure is a part of success also, i am fine")
f.close()

f = open("PYTHON", "r")
print(f.readline())
f.close()
```

## Q15 (Writelines)
**Question:** Demonstrate writing a list of strings to a file using writelines().

**Code (`a8q15_writelines_demo.py`):**
```python
f = open("PYTHON", "w")

description = ["we either choose the pain of discipline \n","or\n","the pain of regret\n"]

f.writelines(description)
f.close()

f = open("PYTHON", "r")
print(f.read())
f.close()
```

## Q16 (Stack Implementation)
**Question:** Implement a Stack using a Python list.

**Code (`a8q16_stack_implementation.py`):**
```python
stack = [10,20,30,40]

def push(x):
    stack.append(x)

def pop():
    if len(stack) == 0:
        return "Underflow"
    return stack.pop()


push(60)
print(pop())
```

## Q17 (Queue Implementation)
**Question:** Implement a Queue using a Python list.

**Code (`a8q17_queue_implementation.py`):**
```python
queue = []

def insert(x):
    queue.append(x)

def delete():
    if len(queue) == 0:
        return "Underflow"
    return queue.pop(0)

insert(10)
insert(20)
insert(30)
print(delete()) 
```
