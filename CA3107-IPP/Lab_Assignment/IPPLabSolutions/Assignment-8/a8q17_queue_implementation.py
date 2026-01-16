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