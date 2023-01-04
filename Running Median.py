#You are given a stream of numbers. Compute the median for each new element .



#Eg. Given [2, 1, 4, 7, 2, 0, 5], the algorithm should output [2, 1.5, 2, 3.0, 2, 2, 2]

import statistics

current_med=[]

def running_median(stream):

  # Fill this in.

  for num in stream:

    current_med.append(num)

    print(statistics.median(current_med))

    

running_median([2, 1, 4, 7, 2, 0, 5])

# 2 1.5 2 3.0 2 2.0 2
