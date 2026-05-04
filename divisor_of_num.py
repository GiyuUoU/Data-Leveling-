'''
Divisors of a Number

You are given an integer n. You need to find all the divisors of n. Return all the divisors of n as an array or list in a sorted order.
A number which completely divides another number is called it's divisor.

Example 1
Input: n = 6
Output = [1, 2, 3, 6]
Explanation: The divisors of 6 are 1, 2, 3, 6.

Example 2
Input: n = 8
Output: [1, 2, 4, 8]
Explanation: The divisors of 8 are 1, 2, 4, 8.
'''
def divisors(n):
    divisor_list = []
    for i in range(1 , n+1):
        if n%i == 0 :
            divisor_list.append(i)
    return divisor_list  # O(n) time complexity

# Optimized approach
def divisors(n):
    divisor_list = []
    for i in range(1 , int(n**0.5)+1):
        if n%i == 0 :
            divisor_list.append(i)
            if i != n//i:  # To avoid adding the square root twice
                divisor_list.append(n//i)
    return sorted(divisor_list)  # O(sqrt(n)) time complexity