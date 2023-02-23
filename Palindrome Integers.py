# Given an integer, check if that integer is a palindrome. For this problem do not convert the integer to a string to check if it is a palindrome.
import math
def is_palindrome(n):
  # Fill this in.
  temp = n
  rev = 0
  while(n>0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
    
  if temp == rev:
  	return True
  else:
  	return False
    
print(is_palindrome(1234321))
# True
print(is_palindrome(1234322))
# False
