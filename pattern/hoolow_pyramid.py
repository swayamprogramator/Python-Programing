def pattern(n):
   for i in range(n):
      for j in range(n-i-1):
         print(" ", end=" ")
      
      for j in range(2*i+1):
         # printing stars
         if j == 0 or j == 2*i:
            print("*", end=" ")
         else:
            if i == n-1:
               print("*", end=" ")
            else:
               print(" ", end=" ")
      print()
 
n = int(input('Enter the number of rows: '))
pattern(n)