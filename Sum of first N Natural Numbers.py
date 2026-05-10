'''
Sum of first N Natural Numbers
Problem Description: Given an integer N, write a program to find the sum of first N natural numbers.

Input: N=5
Output: 15
Explanation: 1+2+3+4+5=15

Input: N=6
Output: 21
Explanation: 1+2+3+4+5+6=15
'''
#brute force approach
def sum_n(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total

# formula approach
def sum_n(n):
    return (n * (n + 1)) // 2

# Recursion approach
def sum_n(n):
    if n == 1:
        return 1

    return n + sum_n(n - 1)