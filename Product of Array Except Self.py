#You are given an array of integers. Return an array of the same size where the element at each index is the product of all the elements in the original array except for the element at that index.



#For example, an input of [1, 2, 3, 4, 5] should return [120, 60, 40, 30, 24].

import numpy

new_list=[]

def products(nums):

  # Fill this in.

  for num in nums:

    temp_list = [i for i in nums if i != num]

    new_list.append(numpy.prod(temp_list))



  return new_list



print(products([1, 2, 3, 4, 5]))

# [120, 60, 40, 30, 24]
