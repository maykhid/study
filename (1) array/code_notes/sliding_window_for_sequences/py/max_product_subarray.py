# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# A subarray is a contiguous subsequence of the array.

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maxi = float('-inf')
        currentWindowProduct = 1
        windowStart = 0

        if(len(nums) == 1):
            return nums[0]

        # check from index 0 -> index n-1 forward
        for fromStart in nums:
            currentWindowProduct *= fromStart
            maxi = max(currentWindowProduct, maxi, fromStart)
            if(currentWindowProduct == 0):
                currentWindowProduct = 1

        currentWindowProduct = 1 # reset cureentWindowProduct

        # check from index index n-1  -> 0 backwards 
        for fromEnd in range(len(nums) - 1, -1, -1):
            currentWindowProduct *= nums[fromEnd]
            maxi = max(currentWindowProduct, maxi, nums[fromEnd])
            if(currentWindowProduct == 0):
                currentWindowProduct = 1

        return maxi

print(Solution.maxProduct(Solution, [1, 2, 3, 4, 0, 5, 6, 3]))