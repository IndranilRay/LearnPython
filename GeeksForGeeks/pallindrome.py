"""
WAP to check if a number is pallindrome
"""


def check_no_is_pallindrome(num=0):
    rev = 0
    temp = num
    while temp != 0:
        remainder = temp % 10
        rev = rev*10 + remainder
        temp = temp//10
    print(temp)
    print(rev, num)
    return rev == num


print(check_no_is_pallindrome(363))
