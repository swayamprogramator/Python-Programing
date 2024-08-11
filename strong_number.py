#sum of factorial of all digits of a number is equal to the number itslef is known as strong number
number = int(input("Enter number: "))
s = 0
temp = number
while(temp > 0):
   fact = 1
   rem = temp % 10
   for i in range(1, rem + 1):
      fact = fact * i
   print("Factorial of %d = %d " %(rem, fact))
   s = s +fact
   temp = temp // 10

print("Sum of factorials of the number %d = %d " %(number,s))
if(s == number):
   print("Strong Number")
else:
   print("Not a strong number")