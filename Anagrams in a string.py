# Given 2 strings s and t, find and return all indexes in string s where t is an anagram
stack = []
def find_anagrams(s, t):
  # Fill this in.
  for k, v in enumerate(s):
      # Create a three(3) letter combination (based on the index plus length of 't') --> sorted --> joined to make a string and append to stack
      stack.append(''.join(sorted(s[k:k+len(t)])))
  
  # print(stack) // to view the items from stack
  # Iterate on all those combinations and return the index of the equal combi
  return [k for k, v in enumerate(stack) if v == t]
  #I had fun
          
print(find_anagrams('acdbacdacb', 'abc'))
# [3, 7]
