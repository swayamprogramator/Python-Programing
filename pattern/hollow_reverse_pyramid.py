def pattern(n):
   for i in range(1, n+1):
      for j in range(0, i):
         print(" ", end=" ")

      for j in range(1, (n*2 - (2*i-1)) + 1):
         if i == 1 or j == 1 or j ==(n*2 -(2*i-1)):
            # printing stars
            print("*", end=" ")
         else:
            print(" ", end=" ")
      print()

n = int(input('Enter the number of rows: '))
pattern(n)