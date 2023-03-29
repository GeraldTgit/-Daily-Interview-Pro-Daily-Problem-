# Given a list of possible coins in cents, and an amount (in cents) n, return the minimum number of coins needed to create the amount n. If it is not possible to create the amount using the given coin denomination, return None.

def make_change(coins, n):
  # Fill this in.
  coins.sort(reverse=True)
  stack=coins
  for coin in coins:
      if x(coin,stack) == n:
          stack.remove(coin)
          computation = " + ".join([str(num) for num in stack])
          return f"{len(stack)} coins ({computation})"
          
x = lambda coin,stack: sum(stack) - coin 

print(make_change([1, 5, 10, 25], 36))
# 3 coins (25 + 10 + 1)
