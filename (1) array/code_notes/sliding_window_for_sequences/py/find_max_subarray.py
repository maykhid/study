# - Fixed length sliding window as the name implies simply means that the “size” of the pointers moving along the sequence remains the same throughout it’s traversal. 
# The code snippet below is an example of fixed length.

# Given an array/list and also given a fixed pointer size k. Find the max sum subarray.
# i.e find a subarray of size '3' (3 numbers) that gives the highest value from the list/array given.
def findMaxSumSubarray(arr: list[int], k: int) -> int:
    maxValue = float('-inf') # init maxvalue with the lowest possible integer
    currentRunningSum = 0
    
    for i, v in enumerate(arr):
        currentRunningSum += v # stores the current runnung sum
        if(i >= k - 1): # basically when we get to a point where we have i >= k - 1 (3 - 1) elements do
            maxValue = max(maxValue, currentRunningSum) # get the maxvalue
            currentRunningSum -= arr[i - (k - 1)] # minus the first check value this iteration
    return maxValue

print(findMaxSumSubarray([4, 2, 1, 7, 8, 1, 2, 8, 1, 0], 3))



