'''
Reverse a given Array
Problem Statement: You are given an array. The task is to reverse the array and print it.

Examples

Input: N = 5, arr[] = {5,4,3,2,1}
Output: {1,2,3,4,5}
Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

Input: N=6 arr[] = {10,20,30,40}
Output: {40,30,20,10}
Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.
'''

# iterative approach
def reverse_array(arr, n):

    start = 0
    end = n - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr
# TC- O(N) , SC- O(1)

# Optimized approach: two pointer 
def reverse_array(arr, n):

    left = 0
    right = n - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr
# TC- O(N) , SC- O(1)