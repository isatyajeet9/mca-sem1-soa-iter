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