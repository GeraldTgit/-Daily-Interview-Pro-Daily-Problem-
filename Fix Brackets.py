#Given a string with only ( and ), find the minimum number of characters to add or subtract to fix the string such that the brackets are balanced.
#The fixed string could either be ()() by deleting the first bracket, or (()()) by adding a bracket. These are not the only ways of fixing the string, there are many other ways by adding it in different positions!

import re
def fix_brackets(s):
  # Fill this in.
    open_parenth = re.findall(r"\(", s)
    close_parenth = re.findall(r"\)", s)
    if len(open_parenth) > len(close_parenth):
    	result = len(open_parenth) - len(close_parenth)
    else:
    	result = len(close_parenth) - len(open_parenth)
    return  result
    
print(fix_brackets('((()())))'))
# 1
