# A3Q4
# Question: Consider the function: def nMultiple(a = 0, num = 1): return a*num
#           What will be the output produced when the following calls are made:
#           nMultiple(5), nMultiple(5,6), nMultiple(num=7), nMultiple(num=6,a=5), nMultiple(5,num=6)
# Name: Satyajeet Nayak
# Appl No: 25C200429
def nMultiple(a=0, num=1):
    return a*num

print("a:", nMultiple(5))
print("b:", nMultiple(5,6))
print("c:", nMultiple(num=7))
print("d:", nMultiple(num=6, a=5))
print("e:", nMultiple(5, num=6))
