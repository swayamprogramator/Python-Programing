x = int(input('Enter First Number: '))
y = int(input('Enter Second Number: '))

if x > y:
    smaller = y
else:
    smaller = x
    
# find gcd of the number
for i in range (1,smaller+1):
    if((x % i == 0) and (y % i == 0)):
        gcd = i

print('The GCD of',x,'and',y,'is',gcd)