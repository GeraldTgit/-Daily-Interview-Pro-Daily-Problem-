#  Given a list of undirected edges which represents a graph, find out the number of connected components.
def num_connected_components(edges):
	# Fill this in.
	stack=0
	# Iterating through edges in dict
	for k, v in enumerate(edges):
	    # Try except block to handle exception when it can no longer iterate in list
	    try:
	        diff1 = edges[k][0] - edges[k][1]
	        diff2 = edges[k][1] - edges[k+1][0]
	        if diff1 and diff2 > 1 or diff1 and diff2 < -1:
	            stack+=1
	    except:
	        if diff1 and diff2 > 1 or diff1 and diff2 < -1:
	            stack+=1

	return stack

print(num_connected_components([(1, 2), (2, 3), (4, 1), (5, 6)]))
# 2
