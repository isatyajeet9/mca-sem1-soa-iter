print("\nFUNCTIONS & SCOPE\n")

x = 10
def func():
    print(x)
func()

x = 5
def func():
    x = 10
    print(x)
func()
print(x)

x = 5
def func():
    global x
    x += 5
func()
print(x)

def outer():
    x = 5
    def inner():
        nonlocal x
        x += 1
        print(x)
    inner()
    print(x)
outer()

