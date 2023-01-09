#Given two arrays, write a function to compute their intersection - the intersection means the numbers that are in both arrays.



#Example 1:

#Input: nums1 = [1,2,2,1], nums2 = [2,2]

#Output: [2]

#Example 2:

#Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]

#Output: [9,4]



#Each element in the result must be unique.

#The result can be in any order.



class Solution:

  def intersection(self, nums1, nums2):

    # Fill this in.

    self=[]

    for num in nums1:

        if num in nums2:

            self.append(num)

    return self



print(Solution().intersection([9, 4, 9, 8, 4], [9, 4, 5]))

# [9, 4]
