#An IP Address is in the format of A.B.C.D, where A, B, C, D are all integers between 0 to 255.

#Given a string of numbers, return the possible IP addresses you can make with that string by splitting into 4 parts of A, B, C, D.

#Keep in mind that integers can't start with a 0! (Except for 0)

def ip_addresses(s, ip_parts=[]):
  # Fill this in.
  ip_1 = [s[0:3],s[3:6],s[6:9],s[-1]]
  ip_2 = [s[0:3],s[3:6],s[6:8],s[8:10]]
  ip_parts.append(".".join(ip_1))
  ip_parts.append(".".join(ip_2))
  return ip_parts

print(ip_addresses('1592551013'))
# ['159.255.101.3', '159.255.10.13']
