# Given a list of strings, find the list of characters that appear in all strings
stack=[]
def common_characters(strs):
  # Fill this in.
  strs_0 = ''.join(set(strs[0])) 
  
  for letter in strs_0:
      for string in strs[1:]:
          if letter in string and letter not in stack:
              stack.append(letter)
                  
  return stack
      
print(common_characters(['google', 'facebook', 'youtube']))
# ['e', 'o']
