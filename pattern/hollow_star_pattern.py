def pattern(n):
   for i in range(n):
      for j in range(n):
         # printing stars
         if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
         else:
            print(" ", end=" ")
      print("\r")
 
n = int(input('Enter the number of rows: '))
pattern(n)