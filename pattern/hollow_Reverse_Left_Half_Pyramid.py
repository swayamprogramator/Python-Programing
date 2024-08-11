def pattern(n):
   for i in range(n, 0, -1):
      for j in range(i, 0, -1):
         if i == 1 or i == n or j == 1 or j == i:
            # printing stars
            print("*", end=" ")
         else:
            print(" ", end=" ")
      print()

n = int(input('Enter the number of rows: '))
pattern(n)