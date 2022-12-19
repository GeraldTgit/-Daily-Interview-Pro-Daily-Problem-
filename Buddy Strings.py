#Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.
class Solution:
  def buddyStrings(self, A, B):
    # Fill this in.
    acount = A.count('a')
    bcount = A.count('b')
    ccount = A.count('c')
    abcount = B.count('a')
    bbcount = B.count('b')
    cbcount = B.count('c')
  
    A = "a: {} b: {} c:{}".format(acount,bcount,ccount)         
    B = "a: {} b: {} c:{}".format(abcount,bbcount,cbcount)  

    if A == B:
        return True
    return False

print(Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
# True
print(Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))
# False