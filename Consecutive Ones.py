#Return the longest run of 1s for a given integer n's binary representation.
#242 in binary is 0b11110010, so the longest run of 1 is 4.

def longest_run(n):
  # Fill this in.
  bin_a = bin(n)
  # Convert binary to string
  binary_str = str(bin_a)
  # Replacing 'b' by by ''
  substrings = binary_str.replace("b", "")
  # Split string by '0'
  substrings = substrings.split('0')
  # Find length of longest substring
  max_length = max([len(substring) for substring in substrings])
  return max_length

print(longest_run(242))
# 4
