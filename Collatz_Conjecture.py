# A recursive function of the Collatz Conjecture.

number = int(input("Pick a number:"))


def collatz(n):
    """Takes any int and returns 1, as per Collatz Conjecture."""
    print(n)
    if n == 1:
        return n
    elif n % 2 == 0:
        return collatz(n/2)
    else:
        return collatz(3*n + 1)


collatz(number)