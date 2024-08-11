def pattern(n):
   for i in range(n):
      for j in range(n-i-1):
         # printing spaces
         print(" ", end=" ")

      for j in range(i+1):
         # printing stars
         print("* ",end="")
      print()
 
n = int(input('Enter the number of rows: '))
pattern(n)