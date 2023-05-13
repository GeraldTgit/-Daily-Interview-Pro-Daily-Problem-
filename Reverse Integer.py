# Given an integer, reverse the digits. Do not convert the integer into a string and reverse it.
def reverse_integer(num):
  # Fill this in.
  reversed_num = 0
  if num  > 0:
      while num != 0:
          digit = num % 10
          reversed_num = reversed_num * 10 + digit
          num //= 10
        
      return reversed_num
  else:
      num = num * -1
      while num != 0:
          digit = num % 10
          reversed_num = reversed_num * 10 + digit
          num //= 10
          
      reversed_num = reversed_num * -1    
      return reversed_num
      
print(reverse_integer(135))
# 531

print(reverse_integer(-321))
# -123
