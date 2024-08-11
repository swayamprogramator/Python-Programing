def digits_count(n):
   i = 0
   while n > 0:
      n //= 10
      i += 1
   return i

def sum(n):
   i = digits_count(n)
   s = 0
   while n > 0:
      digit = n%10
      n //= 10
      s += pow(digit,i)
   return s

num = int(input("Enter number: "))

s = sum(num)

if s == num:
   print("The number is an Armstrong number.")
else:
   print("The number is not an Armstrong number.")