def factorial(num):
   if(num == 0 or num == 1):
      fact = 1
   else:
      fact = num * factorial(num - 1)
   return fact

def strong_num(list):
   list1 = []
   for x in list:
      temp = x
      sum = 0
      while(temp):
         remainder = temp % 10
         sum += factorial(remainder)
         temp = temp // 10
      if(sum == x):
         list1.append(x)
      else:
         pass
   return list1

list = [9,7,6,4,1,2,145]
strong = strong_num(list)
print(strong)