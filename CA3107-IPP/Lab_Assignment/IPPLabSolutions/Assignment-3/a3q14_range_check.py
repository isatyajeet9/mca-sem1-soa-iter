# A3Q14
# Name: Satyajeet Nayak
def inRange(num, low, high):
    return low <= num <= high

num = int(input("Enter number: "))
low = int(input("Enter lower range: "))
high = int(input("Enter upper range: "))
print("Number in range?", inRange(num, low, high))
