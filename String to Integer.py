# Given a string, convert it to an integer without using the builtin str function. You are allowed to use ord to convert a character to ASCII code.
#Consider all possible cases of an integer. In the case where the string is not a valid integer, return None.

def convert_to_int(s):
    if s == '':
        return None
      
    sign = 1
    if s[0] == '-':
        sign = -1
        s = s[1:]
        
    result = 0    
    for c in s:
        if c < '0' or c > '9':
            return None
        result = result * 10 + ord(c) - ord('0')
        
    return sign * result

try:
    print(convert_to_int('-105') + 1)
except TypeError:
    print("None")
# -104
