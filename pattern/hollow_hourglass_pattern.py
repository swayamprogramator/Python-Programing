def pattern(n):
   # print upper hollow hourglass
   for i in range(n, 0, -1):
      for j in range(n-i):
         print(" ", end=" ")
      for j in range(1, 2*i):
         if i==1 or i==n or j==1 or j==2*i-1:
            # printing stars
            print("*", end=" ")
         else:
            print(" ", end=" ")
      print()
   
   # print lower hollow hourglass
   for i in range(2, n+1):
      for j in range(n-i):
         print(" ", end=" ")
      for j in range(1, 2*i):
         if i==n or j==1 or j==2*i-1:
            # printing stars
            print("*", end=" ")
         else:
            print(" ", end=" ")
      print()

n = int(input('Enter the number of rows: '))
pattern(n)