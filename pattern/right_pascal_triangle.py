def pattern(n):
   # print upper triangle
   for i in range(n):
      for j in range(i+1):
         # printing stars
         print("* ",end="")
      print("\r")
      
   # print lower triangle
   for i in range(n):
      for j in range(n-i-1):
         # printing stars
         print("* ",end="")
      print("\r")
 
n = int(input('Enter the number of rows: '))
pattern(n)