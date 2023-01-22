#The h-index is a metric that attempts to measure the productivity and citation impact of the publication of a scholar. The definition of the h-index is if a scholar has at least h of their papers cited h times.



#Given a list of publications of the number of citations a scholar has, find their h-index.



def hIndex(publications):

  # Fill this in.

  publications.sort(reverse=True)

  for k, v in enumerate(publications):

    if k + 1 == v:

        return v



print(hIndex([5, 4, 2, 1, 3]))

# 3
