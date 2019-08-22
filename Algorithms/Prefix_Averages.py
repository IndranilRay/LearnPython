"""
    WAP to calculate Prefix Averages of a sequence of numbers.
    Given a sequence S , consisting of n numbers , we want to compute a sequence A
    such that , A[j] is the average of elements S[0],...,S[j] , for j = 0,...,n-1
"""


def prefix_averages1(input_sequence: list)->list:
    """
    Method return list such that, for all j, A[j] equals average of S[0]....S[j]
    :return: list
   """
    n = len(input_sequence)
    A = [0] * n
    for j in range(n):
        total = 0
        for i in range(j+1):
            total += input_sequence[i]
        A[j] = total/(j+1)
    return A


def prefix_averages2(input_sequence: list)->list:
    """
    Function returns list such that for all j, A[j] equals to avg of S[0],S[1],..,S[j]
    :param input_sequence:
    :return: list
    """
    m = len(input_sequence)
    A = [0] * m
    for j in range(m):
        total = sum(input_sequence[0:j+1])
        A[j] = total/(j+1)
    return A


def prefix_averages3(input_sequence: list)->list:
    """
    Function returns list such that for all j, A[j] equals to avg of S[0],S[1],...,S[j]
    :param input_sequence:
    :return: list
    """
    total = 0
    A = [0] * len(input_sequence)
    m = len(input_sequence)
    for i in range(m):
        total += input_sequence[i]
        A[i] = total/(i+1)

    return A


if __name__ == "__main__":
    prefix_averages1 = prefix_averages1([5, 3, 6, 7, 2, 9])
    print(prefix_averages1, end="\n")
    print("Prefix averages with quadratic time function")
    prefix_averages2 = prefix_averages2([5, 3, 6, 7, 2, 9])
    print(prefix_averages2)
    print("Prefix averages with linear time function")
    prefix_averages3 = prefix_averages3([5, 3, 6, 7, 2, 9])
    print(prefix_averages3)


