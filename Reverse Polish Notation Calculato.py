#Given an expression (as a list) in reverse polish notation, evaluate the expression. Reverse polish notation is where the numbers come before the operand. Note that there can be the 4 operands '+', '-', '*', '/'. You can also assume the expression will be well formed.
#The equivalent expression of the above reverse polish notation would be (1 - ((2 + 3) * 2)).

def reverse_polish_notation(expr):
  # Fill this in.
  stack=[]
  for i in expr:
      if isinstance(i,int):
          stack.append(i)
      else:
          result = eval(str(stack[-2]) + i + str(stack[-1]))
          stack.pop()
          stack.pop()
          stack.append(result)
          
  return stack.pop()
  
# 1 - (2 + 3) * 2
print(reverse_polish_notation([1, 2, 3, '+', 2, '*', '-']))
# -9
