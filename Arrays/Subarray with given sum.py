# Subarray with given sum 
# Easy         Accuracy: 39.71%

# Given an unsorted array A of size N that contains only non-negative integers, 
# find a continuous sub-array which adds to a given number S.

# Example 1:
    # Input:
    # N = 5, S = 12
    # A[] = {1,2,3,7,5}
    # Output: 2 4
    # Explanation: The sum of elements 
    # from 2nd position to 4th position 
    # is 12.
 
# Example 2:
    # Input:
    # N = 10, S = 15
    # A[] = {1,2,3,4,5,6,7,8,9,10}
    # Output: 1 5
    # Explanation: The sum of elements 
    # from 1st position to 5th position
    # is 15.
 

# Your Task:
    # You don't need to read input or print anything. 
    # The task is to complete the function subarraySum() which takes arr, 
    # N and S as input parameters and returns a list containing the starting 
    # and ending positions of the first such occurring subarray from the 
    # left where sum equals to S. The two indexes in the list should be 
    # according to 1-based indexing. If no such subarray is found, return -1. 

 
# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)


# Constraints:
# 1 <= N <= 105
# 1 <= Ai <= 1010


# -------------------------------------------------------

# Solution

def subArraySum(arr, n, s): 
    start = 0
    curr_sum = arr[0]
    
    i=1
    while(i <= n):
        while(curr_sum > s and start < i-1):
            curr_sum -= arr[start]
            start += 1
        
        if(curr_sum == s):
            return [start+1, i]
        
        if(i < n):
            curr_sum += arr[i]
        
        i += 1
    
    return [-1]



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            
            ans=subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends