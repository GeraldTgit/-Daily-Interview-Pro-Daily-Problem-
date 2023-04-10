# Given a square 2D matrix (n x n), rotate the matrix by 90 degrees clockwise.
new_mat=[]
def rotate(mat):
  # Fill this in.
  i=0
  try:
      while i < len(mat):
          # Iterating through index of mat depending on its length.
          stack = [first_mat[i] for first_mat in mat[::-1]]
          i+=1
          # Appending stack to new_mat
          new_mat.append(stack)
  
      # Returning new_mat        
      return new_mat
      
  except:
      return "Invalid 2D matrix"

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9,]]
# Looks like
# 1 2 3
# 4 5 6
# 7 8 9

# Looks like
# 7 4 1
# 8 5 2
# 9 6 3
print(rotate(mat))
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
