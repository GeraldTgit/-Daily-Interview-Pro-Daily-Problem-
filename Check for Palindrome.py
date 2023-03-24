# Given a string, determine if there is a way to arrange the string such that the string is a palindrome. If such arrangement exists, return a palindrome (There could be many arrangements). Otherwise return None.
def find_palindrome(s):
  # Fill this in.
  if s[::-1] == s:
      return s

print(find_palindrome('momom'))
# momom
