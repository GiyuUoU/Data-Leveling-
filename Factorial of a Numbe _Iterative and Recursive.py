'''
Factorial of a Number : Iterative and Recursive
Problem Statement: Given a number X,  print its factorial.
To obtain the factorial of a number, it has to be multiplied by all the whole numbers preceding it. More precisely X! = X*(X-1)*(X-2) … 1.
Note: X  is always a positive number. 
'''

# iterative approach
def factorial(n):

    ans = 1

    for i in range(1, n + 1):
        ans *= i

    return ans

# TC- O(N) , SC- O(1) 

# recursive approach
def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n - 1)