num = int(input('Enter an integer number: '))

# calculate reverse of number
reverse = 0
while(num > 0):
    last_digit = num % 10
    reverse = reverse * 10 + last_digit
    num = num // 10

# display result
print('The reverse number is = ', reverse)
