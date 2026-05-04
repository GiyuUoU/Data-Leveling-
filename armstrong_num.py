'''
Check if the Number is Armstrong
You are given an integer n. You need to check whether it is an armstrong number or not. Return true if it is an armstrong number, otherwise return false.

An armstrong number is a number which is equal to the sum of the digits of the number, raised to the power of the number of digits.

Example 1
Input: n = 153
Output: true
Explanation: Number of digits : 3.
13 + 53 + 33 = 1 + 125 + 27 = 153.
Therefore, it is an Armstrong number.

Example 2
Input: n = 12
Output: false
Explanation: Number of digits : 2.
'''
def armstrong(n):
    digits = len(str(n))
    temp = n 
    sum = 0

    while temp > 0 :
        digit = temp % 10
        sum += digit ** digits
        temp //= 10
    return sum == n