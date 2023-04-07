# Given a list of words in a string, reverse the words in-place (ie don't create a new string and reverse the words). Since python strings are not mutable, you can assume the input will be a mutable sequence (like list).
def reverse_words(words):
  # Fill this in.'
  # Reverse existing list of string then convert it to another list per word but in reversed
  words = ''.join(words[::-1]).split()
  # Reversed word in words to make it readable
  stack = [word[::-1] for word in words]
  # Finally, create another string with spaces and make it a list again. I will not make it another list, only if the 'print' line was not given to me this way.
  return list(' '.join(stack))

s = list("can you read this")
print(''.join(reverse_words(s)))
# this read you can
