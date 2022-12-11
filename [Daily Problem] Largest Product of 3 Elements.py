#You are given an array of integers. Return the largest product that can be made by multiplying any 3 integers in the array.
#Example:
#[-4, -4, 2, 8] should return 128 as the largest product can be made by multiplying -4 * -4 * 8 = 128.

def maximum_product_of_three(lst):
  # Fill this in.
  new_lst = []
  for i in lst:
    if i > 0:
        new_lst.append(i)  
    else:
        i = i * -1
        new_lst.append(i)

  new_lst.sort()
  a = new_lst[-3] * new_lst[-2] * new_lst[-1]
  return a
    

print(maximum_product_of_three([-4, -4, 2, 8]))
# 128