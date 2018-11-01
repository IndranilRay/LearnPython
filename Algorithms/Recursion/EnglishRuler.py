"""
English Ruler is simple example of Fractal , that is a shape that has a self-recursive
nature at various levels of magnification
"""
import sys


def draw_line(tick_length, tick_label=''):
    """ Draw one line with given tick_length and tick_label if provided"""

    line = '-' * tick_length

    if tick_label:
        line += ' ' + tick_label
    sys.stdout.flush()
    print(line)


def draw_interval(central_length):
    """Draw tick interval based upon a central tick_length"""
    if central_length > 0: # stop when length drops to 0
        draw_interval(central_length - 1) # recursively draw top interval
        draw_line(central_length) # draw center tick
        draw_interval(central_length - 1) # recursively draw lower tick


def draw_ruler(no_of_inches, major_length):
    """Draw english ruler with given no_of_inches and major length"""
    draw_line(4, '0')
    for j in range(1, no_of_inches + 1):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))


if __name__ == '__main__':
    draw_ruler(2, 4)




