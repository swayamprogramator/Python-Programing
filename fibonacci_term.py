num = int(input('Enter number of terms: '))

# print fibonacci term
a, b = 0, 1
    
# check if the number of terms is valid
if num <= 0:
    print('Please enter a positive integer.')

elif num == 1:
    print('The Fibonacci term is = ', end='')
    print(a)

else:
    print('The Fibonacci term is = ', end='')
    for i in range (2, num):
        c = a + b
        a = b
        b = c
    print(b)