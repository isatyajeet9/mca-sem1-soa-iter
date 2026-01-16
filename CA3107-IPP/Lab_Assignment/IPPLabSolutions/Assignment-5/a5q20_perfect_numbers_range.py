# Q20
for num in range(1, 501):
    sum_div = 0
    for i in range(1, num):
        if num % i == 0:
            sum_div += i
    if sum_div == num:
        print(num, "is a perfect number")
