#Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.



class Solution:

  def reverseWords(self, str):

    # Fill this in.

    str = list(str.split(" "))

    str_lst=[]

    for word in str:

        str_lst.append(word[::-1])



    str=" "

    

    return str.join(str_lst)



print(Solution().reverseWords("The cat in the hat"))

# ehT tac ni eht tah
