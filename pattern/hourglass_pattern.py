def pattern(n):
   # print downward pyramid
   for i in range(n-1):
      for j in range(i):
         print(" ", end=" ")
      for j in range(2*(n-i)-1):
         # printing stars
         print("*", end=" ")
      print()

   # print upper pyramid
   for i in range(n):
      for j in range(n-i-1):
         print(" ", end=" ")
      for j in range(2*i+1):
         # printing stars
         print("*", end=" ")
      print()

n = int(input('Enter the number of rows: '))
pattern(n)