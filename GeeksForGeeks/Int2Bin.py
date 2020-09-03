"""
Program displays binary equivalent of an integer > 0
"""


def display_bin(n):
    if n == 0:
        return
    display_bin(n//2)
    print(n % 2)


if __name__ == "__main__":
    number = input("Enter a number")
    display_bin(int(number))
