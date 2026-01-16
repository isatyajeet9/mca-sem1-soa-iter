print("\nBUILT-IN FUNCTIONS\n")

import math

print(math.floor(1.6))
print(round(3.567, 2))
print(sorted([4, 1, 6, 3], reverse=True))
print(all([True, True, False]))
print(any([False, 0, [], None]))

print(list(range(5)))
print(chr(65))
print(ord('A'))
print(int('100'))
print(str(123))
print(eval('2+3*4'))

a = [1, 2, 3]
b = ['x', 'y', 'z']
print(list(zip(a, b)))

s = "pythonprogramming"
print(s.capitalize())
print(s.title())

s = "banana"
print(s.count('a'))
print(s.find('a'))
print(s.rfind('a'))
print(s.index('n'))
print(s.replace('a', 'o'))

s = " hello "
print(s.strip())
print(s.lstrip())
print(s.rstrip())

s = "a,b,c"
print(s.split(','))

lst = ['a', 'b', 'c']
print('-'.join(lst))

s = "Python"
print(s.startswith('P'))
print(s.endswith('n'))

s = "12345"
print(s.isdigit())

s = "Python"
print(s.isalpha())

s = "Python123"
print(s.isalnum())

s = "apple"
print(s.find('P'))

s = "HelloWorld"
print(s.split())

s = "Python"
print('-'.join(s))