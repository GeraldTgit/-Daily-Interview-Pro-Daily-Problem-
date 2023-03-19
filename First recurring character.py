#Given a string, return the first recurring letter that appears. If there are no recurring letters, return None.
def first_recurring_char(s):
  # Fill this in.
  frc = next((l for l in s if s.count(l) > 1), None)
  return frc
  
print(first_recurring_char('qwertty'))
# t

print(first_recurring_char('qwerty'))
# None
