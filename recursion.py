"""
A recursive algorithm must have a base case
A recursive algorithm must change its state and move toward the base case
A recursive algorithm must call itself recursively
"""


# Iterative algorithm that calculates the factorial of a number, n
def iterative_factorial(n):
    the_product = 1
    while n > 0:
        the_product *= n
        n = n - 1
    return the_product


print(iterative_factorial(5))


# Recursive algorithm that calculates the factorial of a number, n
def recursive_factorial(n):
    if n == 0:
        return 1
    return n * recursive_factorial(n - 1)


print(recursive_factorial(5))


# Challenge: Print the numbers from 1 to 10 recursively.
# I will also do this iteratively for practice.

def iterative_printing():
    numbers = 1
    while numbers < 11:
        print(numbers)
        numbers += 1
    return numbers


iterative_printing()


def recursive_printing(n=1):
    if n > 10:
        return
    print(n)
    recursive_printing(n + 1)


recursive_printing()
