"""
    Write a function to implement fibonacci series
"""


def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


if __name__ == "__main__":
    n = 5
    factorial_of_five = factorial(n)
    print(factorial)
