'''
Reverse a number

You are given an integer n. Return the integer formed by placing the digits of n in reverse order.

Example 1
Input: n = 25
Output: 52
Explanation: Reverse of 25 is 52.

Example 2
Input: n = 123
Output: 321
Explanation: Reverse of 123 is 321.
'''

def reverse_number(n):
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    print(rev)
    return rev

reverse_number(345)