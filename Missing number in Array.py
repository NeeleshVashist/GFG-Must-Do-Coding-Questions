# Missing number in array 
# Easy          Accuracy: 42.51% 

# Given an array of size N-1 such that it can only contain distinct 
# integers in the range of 1 to N. Find the missing element.

# Example 1:
#     Input:
#     N = 5
#     A[] = {1,2,3,5}
#     Output: 4

# Example 2:
#     Input:
#     N = 10
#     A[] = {1,2,3,4,5,6,7,8,10}
#     Output: 9

# Your Task :
# Complete the function MissingNumber() that takes array and N as input 
# and returns the value of the missing number.

# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(1).

# Constraints:
# 1 ≤ N ≤ 106
# 1 ≤ A[i] ≤ 106



# ------------------------------------------------------------------------------------

# Solution

#User function Template for python3


def MissingNumber(array,n):
    n += 1  # Incrementing n to n+1 because array index starts from 0
    total = (n*(n-1))//2    # Finding the total... from n to n+1 terms
    array_sum = sum(array)
    return total-array_sum


#{ 
# Driver Code Starts
# Initial Template for Python 3
t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=MissingNumber(a,n)
    print(s)
# } 
# Driver Code Ends