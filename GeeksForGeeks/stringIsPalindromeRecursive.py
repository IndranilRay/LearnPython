"""
 WAP to check if input string is palindrome recursive version
"""


def isPalindrome(input_string, start=0, end=0):
    if start >= end:
        return True
    return (input_string[start] == input_string[end]) and isPalindrome(input_string, start+1, end-1)


if __name__ == '__main__':
    string = input("Enter the string:")
    is_string_palindrome = isPalindrome(string, start=0, end=len(string)-1)

    if is_string_palindrome:
        print('String is Palindrome')
    else:
        print('String is not palindrome')