'''
Print 1 to N using Recursion
Problem Description: Given an integer N, write a program to print numbers from 1 to N.
'''

# Forward Recursion 
def print_numbers(i, n):
    if i > n:
        return

    print(i)
    print_numbers(i + 1, n)

# Backward Recursion (Backtracking)
def print_numbers(i, n):
    if i > n:
        return

    print_numbers(i + 1, n)
    print(i)