

up_to = int(input("Up to what number?"))

def fib(x):
    """Prints the Fibonacci sequence up to a inputted number."""
    a, b = 1, 1

    while b < x:
        print(a)
        a, b = b, a+b

fib(up_to)