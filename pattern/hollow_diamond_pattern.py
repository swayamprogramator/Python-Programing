def pattern(n):
   # print upper hollow pyramid
   for i in range(n):
      for j in range(n-i-1):
         print(" ", end=" ")
      for j in range(2*i+1):
         if j == 0 or j == 2*i:
            # printing stars
            print("*", end=" ")
         else:
            print(" ", end=" ")
      print()

   # print downward hollow pyramid
   for i in range(n-1):
      for j in range(i+1):
         print(" ", end=" ")
      for j in range(2*(n-i-1)-1):
         if j == 0 or j == 2*(n-i-1)-2:
            # printing stars
            print("*", end=" ")
         else:
            print(" ", end=" ")
      print()

n = int(input('Enter the number of rows: '))
pattern(n)