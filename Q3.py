"""
Given a string, write a python function to check if it is
palindrome or not.

A string is said to be palindrome if the reverse
of the string is the same as string. For example, “malayalam” is a
palindrome, but “music” is not a palindrome.
"""


# Approach 1: Splicing
def isPalindrome(s: str):
    if s == s[::-1]:
        return True
    else:
        return False


string = input("Enter a string: ")
print(isPalindrome(string))


# Approach 2: Traditional approach
def isPalindrome_traditional(s: str):
    reverse = ""
    for i in s:
        reverse = i + reverse

    if reverse == s:
        return True
    else:
        return False


string = input("Enter a string: ")
print(isPalindrome_traditional(string))
