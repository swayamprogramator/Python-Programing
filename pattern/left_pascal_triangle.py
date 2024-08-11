def pattern(n):
   # print upper triangle
   for i in range(n):
      for j in range(n-i-1):
         print(" ", end=" ")

      for j in range(i+1):
         print("* ",end="")
      print()

   # print lower triangle
   for i in range(n-1):
      for j in range(i+1):
         print(" ",end=" ")

      for j in range(n-i-1):
         print("* ",end="")
      print()
 
n = int(input('Enter the number of rows: '))
pattern(n)