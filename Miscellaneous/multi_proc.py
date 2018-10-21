"""
Use multi processing module for seperate processes
Note: Every process has its own address space (virtual memory).Thus program
variables are not shared between two processes. You need to use Interprocess
communication technique (IPC) if you want to share data between two process.
"""
import time
import multiprocessing

square_result = []


def calc_square(numbers):
    global square_result
    for n in numbers:
        print("Sqaure:", n*n)
        square_result.append(n*n)
    print("Result in process:", square_result)


def calc_cube(numbers):
    for n in numbers:
        print("Cube:", n*n*n)


if __name__ == '__main__':
    arr = [2, 3, 5, 6]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))

    p1.start()
    p1.join()

    print("Result" + str(square_result))
    print("Done")

