# Given an array of integers of size n, where all elements are between 1 and n inclusive, find all of the elements of [1, n] that do not appear in the array. Some numbers may appear more than once.

class Solution(object):
  def findDisappearedNumbers(self, nums):
    # Fill this in.
    self=[]
    temp_list = list(range(min(nums),max(nums)+1))
    for num in temp_list:
    	if num not in nums:
        	self.append(num)
            
    return self

nums = [4, 6, 2, 6, 7, 2, 1,8]
print(Solution().findDisappearedNumbers(nums))
# [3, 5]
