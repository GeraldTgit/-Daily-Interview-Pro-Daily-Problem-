def findKthLargest(nums, k):
  # Fill this in.
  less_nums = []
  great_nums = []
  # Traversing through nums
  for num in nums:
    if num < k:
        # Creating list for nums less than k
        less_nums.append(num)
    else:
        # Creating list for nums greater than k then sort
        great_nums.append(num)
        great_nums.sort()
  # Combining both lists
  nums = less_nums + great_nums
  # Returning k-th largest. Count from right to left
  return nums[0-k]

print(findKthLargest([3, 5, 2, 4, 6, 8], 3))
# 5
print(findKthLargest([3, 5, 2, 1, 1, 10], 1))
# 10
print(findKthLargest([3, 5, 6, 7, 3, 0], 2))
# 6