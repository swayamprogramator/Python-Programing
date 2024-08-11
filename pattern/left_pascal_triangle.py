def pattern(n):
   # print upper triangle
   for i in range(n):
      for j in range(n-i-1):
         # printing spaces
         print(" ", end=" ")

      for j in range(i+1):
         # printing stars
         print("* ",end="")
      print()

   # print lower triangle
   for i in range(n-1):
      for j in range(i+1):
         # printing spaces
         print(" ",end=" ")

      for j in range(n-i-1):
         # printing stars
         print("* ",end="")
      print()
 
# take inputs
n = int(input('Enter the number of rows: '))

# calling function
pattern(n)