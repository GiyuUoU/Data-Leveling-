'''
Problem Description: Given an integer N, write a program to print your name N times.

Examples
Input: N = 3
Output: Ashish Ashish Ashish 
Explanation: Name is printed 3 times.
Input: N = 1
Output: Ashish 
Explanation: Name is printed once.
'''
def print_name(n):
    for i in range(n):
        print("Ashish", end=" ") # Brute Force Approach - Iterative loop

# Time: O(n) , Space: O(1)

def print_name_recursive(n):
    if n == 0:
        return
    print("Ashish", end=" ") # Recursive Approach
    print_name_recursive(n-1)
    
# Time: O(n) , Space: O(n) - due to recursive stack space