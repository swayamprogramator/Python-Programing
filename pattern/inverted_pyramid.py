def pattern(n):
   # number of spaces
   a = n
   for i in range(n-1, -1, -1):
      for j in range(a, 0, -1):
         print(end=" ")
         
      a = a + 1
      for j in range(0, i+1):
         # printing stars
         print("* ",end="")
      print("\r")
 
n = int(input('Enter the number of rows: '))
pattern(n)