def buy_and_sell(arr):
  #Fill this in.
  #Buy on the lowest low of the stocks
  arr_min = min(arr)
  #Create new list from the time of bought to the end of the day os stock exchange
  new_lst = arr[arr.index(arr_min):len(arr)]
  #Sell on the highest high of the stock from new_list
  arr_max = max(new_lst)
  #Calculate profit Sell - Buy
  profit = arr_max - arr_min
  #Return profit
  return profit

print(buy_and_sell([9, 11, 8, 5, 7, 10]))
# 5
