# Given a non-negative integer n, convert the integer to hexadecimal and return the result as a string. Hexadecimal is a base 16 representation of a number, where the digits are 0123456789ABCDEF. Do not use any builtin base conversion functions like hex.
def to_hex(n):
  # Fill this in.
  stack = []
  Hexadecimal = "0123456789ABCDEF"
  quotient = n
  while quotient > 0:
      quotient //= 16
      remainder = n % 16
      if quotient != 0: 
        stack.append(Hexadecimal[quotient])
      elif remainder <= 16:
        stack.append(Hexadecimal[remainder])
      
  return "".join(stack)
  
print(to_hex(123))
# 7B

print(to_hex(242))
# F2
