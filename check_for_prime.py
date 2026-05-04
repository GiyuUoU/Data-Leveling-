'''
Check for Prime Number

You are given an integer n. You need to check if the number is prime or not. Return true if it is a prime number, otherwise return false.
A prime number is a number which has no divisors except 1 and itself.

Example 1
Input: n = 5
Output: true
Explanation: The only divisors of 5 are 1 and 5 , So the number 5 is prime.

Example 2
Input: n = 8
Output: false
Explanation: The divisors of 8 are 1, 2, 4, 8, thus it is not a prime number.
'''

def is_prime(n):
    count = 0
    
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
            
    return count == 2 #Brute Force Approach, Time Complexity: O(n)

#Optimized Approach, Time Complexity: O(sqrt(n))
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
