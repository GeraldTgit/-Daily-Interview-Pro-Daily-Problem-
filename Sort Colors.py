#Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.



#Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.



#Note: You are not suppose to use the library’s sort function for this problem



class Solution:

  def sortColors(self, nums):

    # Fill this in.

    red=[]

    white=[]

    blue=[]

    for num in nums:

        if num == 0:

            red.append(num)

            

        elif num == 1:

            white.append(num)

            

        else:

            blue.append(num)

            

    red.extend(white)

    red.extend(blue)

    return red



nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

print("Before Sort: ")

print(nums)

# [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]



print("After Sort: ")

print(Solution().sortColors(nums))

# [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]
