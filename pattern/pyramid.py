def pattern(n):
   # number of spaces
   a = n - 1
   for i in range(n):
      for j in range(a):
         print(end=" ")
         
      # decrementing a after each loop
      a = a - 1
      for j in range(i+1):
         # printing stars
         print("* ",end="")
      print("\r")
 
n = int(input('Enter the number of rows: '))
pattern(n)