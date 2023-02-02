# You are given an array of integers. Return all the permutations of this array.

from itertools import permutations
def permute(nums):
  # Fill this in.
  perm = permutations(nums)
  nums=[]
  for num in perm:
  	nums.append(list(num))
    
  return nums
    
print(permute([1, 2, 3]))
# [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]
