# The Fibonacci sequence is the integer sequence defined by the recurrence relation: F(n) = F(n-1) + F(n-2), where F(0) = 0 and F(1) = 1. In other words, the nth Fibonacci number is the sum of the prior two Fibonacci numbers. Below are the first few values of the sequence: 

class Solution():
  def fibonacci(self, n):
    # fill this in.
    fibo=[]
    a, b = 0, 1
    while len(fibo) < n+1:
      fibo.append(a)
      a, b = b, a+b      
    return fibo[n]
   

n = 9
print(Solution().fibonacci(n))
# 34
