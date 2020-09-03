def sum_n_natural_nums(n):
    total_sum = 0
    for i in range(1, n+1):
        total_sum += i
    return total_sum


if __name__ == '__main__':
    total_sum = sum_n_natural_nums(3)
    print(f'Total sum of natural numbers {total_sum}')