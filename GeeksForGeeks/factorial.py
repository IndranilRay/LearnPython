def rec_factorial(n):
    if n == 1:
        return 1
    else:
        return n * rec_factorial(n-1)


def iter_factorial(num):
    result = 1
    if num == 1:
        return 1
    else:
        for i in range(result, num + 1):
            result = result * i
        return result

print(rec_factorial(5))
print(iter_factorial(5))