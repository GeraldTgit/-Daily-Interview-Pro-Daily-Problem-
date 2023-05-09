#Pascal's Triangle is a triangle where all numbers are the sum of the two numbers above it. Here's an example of the Pascal's Triangle of size 5.
#Given an integer n, generate the n-th row of the Pascal's Triangle.
from math import factorial
def pascal_triangle_row(n):
  # Fill this in.
  res = []
  for i in range(n):
      stack = [factorial(i)//(factorial(j)*factorial(i-j)) for j in range(i+1)]
      res.append(stack)
    
  return res[-1]

print(pascal_triangle_row(6))
# [1, 5, 10, 10, 5, 1]
