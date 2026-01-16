stack = [10,20,30,40]

def push(x):
    stack.append(x)

def pop():
    if len(stack) == 0:
        return "Underflow"
    return stack.pop()


push(60)
print(pop())