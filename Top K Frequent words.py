# Given a non-empty list of words, return the k most frequent words. The output should be sorted from highest to lowest frequency, and if two words have the same frequency, the word with lower alphabetical order comes first. Input will contain only lower-case letters.

class Solution(object):
  def topKFrequent(self, words, k):
    # Fill this in.
    temp_dict = {}
    self = []
    i=0
    #Loop in words and create a temporary dict with values as its frequency
    for word in words:
    	if words.count(word) >= k and word not in temp_dict:
            temp_dict[word] = words.count(word)
    
    #Use sorted functin to keys based on their values in ascending order then sort again the keys has equivalent value from the dict.
    temp_dict=dict(sorted(temp_dict.items(), key=lambda item: (-item[1], item[0])))
    #Convert dict to list using the .keys() method
    self = list(temp_dict.keys())
                       
    return self
        	
words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
k = 2
print(Solution().topKFrequent(words, k))
# ['pro', 'daily']
