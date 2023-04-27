#  Given a list of numbers, for each element find the next element that is larger than the current element. Return the answer as a list of indices. If there are no elements larger than the current element, then use -1 instead.
stack = []
def larger_number(nums):
  # Fill this in.
  for num in nums:
      for x in nums[nums.index(num)+1:]:
          if x > num:
              stack.append(nums.index(x))
              break
          
      if any(i > num for i in nums[nums.index(num)+1:]):
          pass
      else:
          stack.append(-1)
          
  return stack
      
# print [2, 2, 3, 4, -1, -1]
print(larger_number([3, 2, 5, 6, 9, 8]))
