# A5Q2
# Question: Find output of various loop constructs (see code comments for each sub-question)
# Name: Satyajeet Nayak
# Appl No: 25C200429

# Q2a
number = 72958476
a, b = 0, 0
while (number > 0):
    digit = number % 10
    if(digit % 2 != 0):
        a += digit
    else:
        b += digit
    number //= 10
print("Q2a=",a, b) 


# Q2b
total = 0
N = 5
for i in range(1, N+1):
    for j in range(1, N+1):
        total += i
print("Q2b:",total)


# Q2c
for i in range(1, 6, 7):
    print("Q2c:",i) 

# Q2d
for i in range(1, 6):
    print("Q2d:",i) 


# Q2e
for i in range(6):
    print("Q2e:",i)

# Q2f
for i in range(2,6):
    print("Q2f:",i) 


# Q2g
for i in range(7,6):
    print("Q2g:",i)


# Q2h
for i in range(5, 0, -1):
    print("Q2h:",i)

# Q2i
result = 1
for i in range(1, 4):
    result *= i
print("Q2i:",result) 


# Q2j
for i in range(20,1):
    print("Q2j:",i)  


# Q2k
for i in range(20,10,-1):
    print("Q2k:",i)


# Q2l
for i in range(20,-1,-1):
    print("Q2l:",i) 


# Q2m
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print("Q2m:",i, end=" ") 


# Q2n
for i in range(1, 6):
    if i % 2 == 0:
        break
    print("Q2n:",i, end=" ") 



# Q2o
for i in range(1, 6):
    if i % 2 == 0:
        pass
    print("Q2o:",i, end=" ")







