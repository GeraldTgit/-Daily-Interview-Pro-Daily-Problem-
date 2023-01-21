#Two words can be 'chained' if the last character of the first word is the same as the first character of the second word.



#Given a list of words, determine if there is a way to 'chain' all the words in a circle.



from collections import defaultdict



def chainedWords(words):

  # Fill this in.

  i=1

  verify=[]

  #Regular loop method because I can't figure out how to use defaultdict 

  while i <= 4:

    if words[i-1][-1] == words[i][0]:

        verify.append(words[i-1])

        i+=1



  if words[0][0] == words[-1][-1]:verify.append(words[-1])

  if words == verify:

    return True

  #else False so it will return false even if it returns None 

  else:

    return False



print(chainedWords(['apple', 'eggs', 'snack', 'karat', 'tunk']))

# True

