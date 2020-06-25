"""
WAP to draw english ruler:
We denote the length of the tick
designating a whole inch as the major tick length. Between the marks for whole
inches, the ruler contains a series of minor ticks, placed at intervals of 1/2 inch,
1/4 inch, and so on. As the size of the interval decreases by half, the tick length
decreases by one.
"""


def draw_ruler(no_of_inches, major_length):
    draw_line(major_length, '0')

    for j in range(1, 1 + no_of_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))


def draw_line(major_length, optional_labels):
    line = '-'*major_length
    if optional_labels:
        line = optional_labels + line
    print(line)


def draw_interval(central_length):
    if central_length > 0:
        draw_interval(central_length - 1)
        draw_line(central_length, '')
        draw_interval(central_length - 1)


if __name__ == "__main__":
    # Here major tick is the key,
    draw_ruler(5, 4)

