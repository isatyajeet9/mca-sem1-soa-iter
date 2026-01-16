# Assignment-5 Questions and Answers

## Q1
**Question:** Write a program that gets three integers from the user. Count from the first number to the second number in increments of the third number.

**Code (`a5q1_range_with_step.py`):**
```python
# A5Q1
# Question: Write a program that gets three integers from the user. Count from the first
#           number to the second number in increments of the third number.
# Name: Satyajeet Nayak
# Appl No: 25C200429

start = int(input("from: "))
end = int(input("to: "))
step = int(input("step by: "))
for i in range(start, end, step):
    print(i, end=" ")
print()
```

## Q2
**Question:** Find output of various loop constructs.

**Code (`a5q2_loop_output_analysis.py`):**
```python
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
```

## Q3
**Question:** Print years from 1990 to 2000, 5 per line.

**Code (`a5q3_year_print_formatted.py`):**
```python
# Q3
count = 0
for i in range(1990, 2001):
    print(i, end=" ")
    count += 1
    if count % 5 == 0:
        print()
```

## Q4
**Question:** Calculate the sum of all numbers below N that are divisible by 3 or 5.

**Code (`a5q4_sum_divisible_3_or_5.py`):**
```python
# Q4
N = int(input("Enter N: "))
total = 0
for i in range(N):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print("Sum:", total)
```

## Q5
**Question:** Print various star patterns.

**Code (`a5q5_star_patterns.py`):**
```python
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()



row=7
for i in range(1, row + 1):
    for j in range(i):
        print(i, end=" ")
    print()



# r = 5
# for i in range(1, r + 1):
#     for j in range(r - i):
#         print(" ", end="")
#     for k in range(2 * i - 1):
#         print("*", end="")
#     print()

n=1
sp=4
for i in range(1,6):
    print(sp*" ", n*'*')
    sp-=1
    n+=2
```

## Q6
**Question:** Print a pattern where '*' is printed if row divides col or col divides row.

**Code (`a5q6_divisor_pattern.py`):**
```python
for i in range(1, 11):
    for j in range(1, 11):
        
        if i % j == 0 or j % i == 0:
            print("*", end="  ")
        else:
            print(" ", end="  ")
    print(i) 
```

## Q7
**Question:** Calculate harmonic mean of n numbers.

**Code (`a5q7_harmonic_mean.py`):**
```python
# Q7
n = int(input("How many numbers? "))
total = 0
for i in range(n):
    x = float(input("Enter number: "))
    total += 1/x
hm = n / total
print("Harmonic Mean:", hm)
```

## Q8
**Question:** Compute sum of alternating series: 1 - 3 + 5 - 7 ... up to n terms.

**Code (`a5q8_alternating_series.py`):**
```python
# Q8
n = int(input("Enter n: "))
s = 0
sign = 1
for i in range(1, 2*n, 2):
    s += sign * i
    sign *= -1
print("Sum S:", s)
```

## Q9
**Question:** Calculate factorial of n.

**Code (`a5q9_factorial.py`):**
```python
# Q9
n = int(input("Enter n: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print(f"{n}! =", fact)
```

## Q10
**Question:** Calculate x^n / n!.

**Code (`a5q10_xn_over_factorial.py`):**
```python
# Q10
x = int(input("Enter x: "))
n = int(input("Enter n: "))
fact = 1
for i in range(1, n+1):
    fact *= i
result = x**n / fact
print("Result:", result)
```

## Q11
**Question:** Print Fibonacci series up to n terms.

**Code (`a5q11_fibonacci_series.py`):**
```python
# Q11
n = int(input("Enter number of terms: "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
```

## Q12
**Question:** Print Tribonacci series up to n terms.

**Code (`a5q12_tribonacci_series.py`):**
```python
# Q12
n = int(input("Enter number of terms: "))
a, b, c = 1, 2, 3
print(a, b, c, end=" ")
for i in range(3, n):
    d = a + b + c
    print(d, end=" ")
    a, b, c = b, c, d
```

## Q13
**Question:** Reverse a positive integer.

**Code (`a5q13_reverse_number.py`):**
```python
# Q13
n = int(input("Enter a positive integer: "))
rev = 0
while n > 0:
    rev = rev*10 + n%10
    n //= 10
print("Reversed:", rev)
```

## Q14
**Question:** Convert a positive integer to binary.

**Code (`a5q14_decimal_to_binary.py`):**
```python
# Q14.
n = int(input("Enter a positive integer: "))
binary = ""
while n > 0:
    binary = str(n % 2) + binary
    n //= 2
print("Binary:", binary)
```

## Q15
**Question:** Calculate GCD of two numbers.

**Code (`a5q15_gcd_calculator.py`):**
```python
# Q15
x = int(input("Enter x: "))
y = int(input("Enter y: "))
while y != 0:
    x, y = y, x % y
print("GCD:", x)
```

## Q16
**Question:** Calculate sum of factorials: 1! + 2! + ... + n!.

**Code (`a5q16_sum_of_factorials.py`):**
```python
# Q16
n = int(input("Enter n: "))
sum_fs = 0
for i in range(n+1):
    fact = 1
    for j in range(1, i+1):
        fact *= j
    sum_fs += fact
print("Sum:", sum_fs)
```

## Q17
**Question:** Calculate sum of exponential series: x + x^2/2! + ... + x^n/n!.

**Code (`a5q17_exponential_series.py`):**
```python
# Q17
x = float(input("Enter x: "))
n = int(input("Enter n: "))
s = 0
for i in range(1, n+1):
    fact = 1
    for j in range(1, i+1):
        fact *= j
    s += x**i / fact
print("Sum:", s)
```

## Q18
**Question:** Calculate sum of sine series: x - x^3/3! + x^5/5! - ...

**Code (`a5q18_sine_series.py`):**
```python
# Q18
x = float(input("Enter x: "))
n = int(input("Enter n: "))
s = 0
sign = 1
for i in range(1, 2*n, 2):
    fact = 1
    for j in range(1, i+1):
        fact *= j
    s += sign * x**i / fact
    sign *= -1
print("Sum:", s)
```

## Q19
**Question:** Calculate sum of digits of an integer.

**Code (`a5q19_digit_sum.py`):**
```python
# Q19
n = int(input("Enter an integer: "))
sum_digits = 0
while n > 0:
    sum_digits += n % 10
    n //= 10
print("Sum of digits:", sum_digits)
```

## Q20
**Question:** Find perfect numbers between 1 and 500.

**Code (`a5q20_perfect_numbers_range.py`):**
```python
# Q20
for num in range(1, 501):
    sum_div = 0
    for i in range(1, num):
        if num % i == 0:
            sum_div += i
    if sum_div == num:
        print(num, "is a perfect number")
```
