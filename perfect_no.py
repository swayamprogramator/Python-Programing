#perfect number->sum of its positive divisor is equal to number itself
N = int(input("Enter a number: "))

# check perfect number
sum = 0 
for i in range(1,N): 
   if(N%i == 0):
      sum = sum+i

# display result
if(sum == N): 
   print(N, "is a perfect number")
else: 