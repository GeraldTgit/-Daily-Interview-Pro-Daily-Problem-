#  Given a list of numbers and an integer k, partition/sort the list such that the all numbers less than k occur before k, and all numbers greater than k occur after the number k.
def partition_list(nums, k):
  # Fill this in.
  nums.sort()
  return nums
  # nailed it!        

print(partition_list([2, 2, 2, 5, 2, 2, 2, 2, 5], 3))
# [2, 2, 2, 2, 2, 2, 2, 2, 5, 5]
