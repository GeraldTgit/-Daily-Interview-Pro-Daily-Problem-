# Given a phone number, return all valid words that can be created using that phone number.
#For instance, given the phone number 364
#we can construct the words ['dog', 'fog'].

lettersMaps = {
    1: [],
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
    0: []
}

validWords = ['dog', 'fish', 'cat', 'fog']

def makeWords(phone):
  #Fill this in
  i=0
  newWords=[]
  while i != len(validWords):
      stack=""
      for l in validWords[i]:
          for n in phone:
              if l in lettersMaps[int(n)]:
                 stack+=l
      i+=1
      if stack in validWords:
          newWords.append(stack)
  return newWords

print(makeWords('364'))
# ['dog', 'fog']
