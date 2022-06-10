

# time O(n^2) space O(n)
# class Solution:
    
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         found = []
#         # create a loop to point at each index
#         for i, v in enumerate(nums):
#             if(v in found):
#                 return True
#             else:
#                 found.append(v)
#         return False

# time O(n) space O(n)
class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums)) # This one liner simply checks if the length of the nums array is equal to the length of set of nums array. A set does not repeat elements, if len(set(nums)) == len(nums)
        # it means no dupes was found


# can it be better than O(n)?

print(Solution.containsDuplicate(Solution, [1,2,2,4]))