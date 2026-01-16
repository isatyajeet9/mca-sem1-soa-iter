print("\nLOOPS OUTPUT\n")

for i in range(1, 6):
    print(i * 2)

for i in range(5, 0, -1):
    print(i)

i = 1
while i <= 5:
    print(i, end="")
    i += 2
print()

i = 5
while i > 0:
    print(i)
    i -= 2

for i in range(5):
    if i % 2 == 0:
        print(i)

for i in range(1, 6):
    if i == 3:
        break
    print(i)

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

for i in range(3):
    for j in range(2):
        print(i, j)

for i in range(1, 4):
    for j in range(1, i + 1):
        print(j, end="")
    print()

for i in range(3):
    print(i)
else:
    print("Done")

i = 1
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1
else:
    print("Finished")

x = 0
for i in range(1, 5):
    x += i
print(x)

count = 0
for i in range(10):
    if i % 3 == 0:
        count += 1
print(count)

i = 0
while i < 3:
    print(i)
    i += 1
else:
    print(i)

for i in range(10, 4, -2):
    print(i)

i = 10
while i > 0:
    print(i, end="")
    i //= 2
print()

lst = [2, 4, 6]
for i in lst:
    print(i * 2)

lst = [1, 2, 3]
for i in range(len(lst)):
    print(lst[i])

