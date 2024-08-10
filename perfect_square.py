import math    

# take inputs
num = int(input('Enter number: '))

root = math.sqrt(num)
# check number is perfecct square
if int(root + 0.5) ** 2 == num:
    print(num, 'is a perfect square')
else: