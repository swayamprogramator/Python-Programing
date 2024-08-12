import numpy

# take inputs
m1 = [[1, 7],
      [4, 5]]

m2 = [[5, 3],
      [4, 2]]

res = [[0, 0],
       [0, 0]]

# multiply matrix
print("Matrix Multiplication: ")
result = m1&m2
for row in result:
   print(row)