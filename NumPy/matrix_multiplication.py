print("Enter the order of matrix 1:")
m, n = list(map(int, input().split()))
print("Enter row values")
m1 = []
for i in range(m):
   print("Enter row",  i, "values:")
   row = list(map(int, input().split()))
   m1.append(row)

# take second matrix inputs
print("Enter the order of matrix2:")
p, q = list(map(int, input().split()))
print("Enter row values")
m2 = []
for j in range(p):
   print("Enter row", j, "value:")
   row = list(map(int, input().split()))
   m2.append(row)

# print both matrices
print("Matrix 1:", m1)
print("Matrix 2:", m2)

# multiply matrix
result = []
for i in range(m):
   row = []
   for j in range(q):
      row.append(0)
   result.append(row)
print("Matrix Multiplication:")
for i in range(m):
   for j in range(q):
      for k in range(n):
         result[i][j] += m1[i][k] * m2[k][j]
for row in result:
   print(row)