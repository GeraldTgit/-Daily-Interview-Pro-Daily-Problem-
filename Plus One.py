#Given a non-empty array where each element represents a digit of a non-negative integer, add one to the integer. The most significant digit is at the front of the array and each element in the array contains only one digit. Furthermore, the integer does not have leading zeros, except in the case of the number '0'.



class Solution():

  def plusOne(self, digits):

    # Fill this in.

    self.digits = digits

    temp_list = [str(num) for num in self.digits]

    temp_list = int(''.join(temp_list)) + 1

    self.digits = [int(num) for num in str(temp_list)]

    return self.digits



num = [2, 9, 9]

print(Solution().plusOne(num))

# [3, 0, 0]
