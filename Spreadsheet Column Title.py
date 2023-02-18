class Solution:
  def convertToTitle(self, n):
    # Fill this in.
    self.n = n
    title = ""
    while self.n != 0:
        self.n = self.n - 1
        #chr() function takes integer argument and return the string representing a character
        #This line takes the modulo of self.n with 26 and adds 65 to it. This will give a number in the range of 65-90 (capital A-Z in ASCII table).
        title = chr(self.n % 26 + 65) + title
        #to prepare for the next iteration of the loop where the remainder after dividing by 26 is used to calculate the next letter in the resulting string
        self.n = self.n // 26
    return title
    	

input1 = 1
input2 = 456976
input3 = 28
print(Solution().convertToTitle(input1))
# A
print(Solution().convertToTitle(input2))
# YYYZ
print(Solution().convertToTitle(input3))
# AB
