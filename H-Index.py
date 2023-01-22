#The h-index is a metric that attempts to measure the productivity and citation impact of the publication of a scholar. The definition of the h-index is if a scholar has at least h of their papers cited h times.



#Given a list of publications of the number of citations a scholar has, find their h-index.



def hIndex(publications):

  # Fill this in.

  publications.sort(reverse=True)

  for k, v in enumerate(publications, start=1):

    #publications[k-1] refers to v

    if k <= v and k-1 < publications[k-2] and k+1 > publications[k]:

      return k



print(hIndex([5, 4, 3, 2, 1]))

#             1, 2, 3, 4, 5

#Answer       3



print(hIndex([10,15,9,5,1]))

#             2, 1, 3,4,5

#Answer       4



print(hIndex([263,84,61,24,15,9,8,5]))

#             1,  2, 3, 4, 5, 6,7,8

#Answer       7



print(hIndex([87,70,46,32,19,15,10,9,8,6,4,1]))

#Answer       8



print(hIndex([33,30,20,15,7,6,5,4]))

#Answer       6
