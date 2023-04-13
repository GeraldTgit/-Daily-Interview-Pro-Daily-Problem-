# Given a sorted list of numbers, and two integers low and high representing the lower and upper bound of a range, return a list of (inclusive) ranges where the numbers are missing. A range should be represented by a tuple in the format of (lower, upper).
stack=[]
def missing_ranges(nums, low, high):
  # Fill this in.
  nums.sort()

  for k, v in enumerate(nums):
      if v == high: return stack
      if v < low: nums.remove(v)
      if nums[k+1] - nums[k] >=2:
          temp = (nums[k]+1,nums[k+1]-1)
          stack.append(temp)
          	  
print(missing_ranges([0.9, 0, 1, 3, 5, 10], 1, 10))
# [(2, 2), (4, 4), (6, 9)]
