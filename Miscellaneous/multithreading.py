"""
Using multi threading  tool
"""
import time
import threading


def calc_square(numbers):
    print("Calculate square numbers")
    for n in numbers:
        time.sleep(0.2)
        print("Square:", n*n)


def calc_cube(numbers):
    print("Calculate cube  numbers")
    for n in numbers:
        time.sleep(0.2)
        print("Cube:", n*n*n)


arr = [2, 3, 8, 7]

t = time.time()

# create thread
t1 = threading.Thread(target=calc_square, args = (arr,))
t2 = threading.Thread(target=calc_cube, args = (arr,))

# this will execute this two programs in parallel
t1.start()
t2.start()

# join will wait untill thread is done
t1.join()
t2.join()


# calc_square(arr)
# calc_cube(arr)

print("done in : ", time.time() - t)
print("Yeh.. I am done with all my work")

# Multi threading is typically used when your CPU is idle
# for ex a web service may take a fee seconds to give you back response
# in that time you can optimize your performance of application




