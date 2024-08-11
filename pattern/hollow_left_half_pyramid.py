def pattern(n):
   for i in range(1, n+1):
      for j in range(i):
         # printing stars
         if j == 0 or j == i-1:
            print("*", end=" ")
         else:
            if i != n:
               print(" ", end=" ")
            else:
               print("*", end=" ")
      print()
 
n = int(input('Enter the number of rows: '))
pattern(n)