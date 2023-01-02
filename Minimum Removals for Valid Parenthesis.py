#You are given a string of parenthesis. Return the minimum number of parenthesis that would need to be removed in order to make the string valid. "Valid" means that each open parenthesis has a matching closed parenthesis.

import re

def count_invalid_parenthesis(string):

  # Fill this in.

  val = re.findall(r"\)\)",string)

  return len(val)



print(count_invalid_parenthesis("()())()"))

# 1
