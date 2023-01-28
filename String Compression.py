#Given an array of characters with repeats, compress it in place. The length after compression should be less than or equal to the original array.



class Solution(object):

  def compress(self, chars):

    # Fill this in.

    self=[]

    for char in chars:

        if char not in self:

            self.append(char)

            if chars.count(char) > 1: self.append(chars.count(char))



    return self



print(Solution().compress(['a', 'a', 'b', 'c', 'c', 'c']))

# ['a', '2', 'b', 'c', '3']
