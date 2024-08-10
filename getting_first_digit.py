num = int(input('Enter any Number: '))

# get the first digit
while (num >= 10):
    num = num // 10

# printing first digit of number
print('The first digit of number:', num)