# Given a list of sorted numbers (can be both negative or positive), return the list of numbers squared in sorted order.
def square_numbers(nums):
 # Fill this in.
 nums = [n * -1 for n in nums if n < 0] + [n for n in nums if n >= 0]
 nums.sort()
 return [n * n for n in nums]

print(square_numbers([-5, -3, -1, 0, 1, 4, 5]))
# [0, 1, 1, 9, 16, 25, 25]
