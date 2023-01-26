#  Given an array of integers, arr, where all numbers occur twice except one number which occurs once, find the number. Your solution should ideally be O(n) time and use constant extra space. 

class Solution(object):
  def findSingle(self, nums):
    # Fill this in.
    for self in nums:
    	if nums.count(self) == 1:
        	return self

nums = [1, 1, 3, 4, 4, 5, 6, 5, 6]
print(Solution().findSingle(nums))
# 3
