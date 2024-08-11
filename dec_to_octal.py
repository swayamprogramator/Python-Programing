def DecimalOctal(num):
    octal, i = 0, 1

    while (num != 0):
        rem = num % 8  
        octal += rem * i
        
        i = i*10
        num //= 8
     
    print(octal)

num = int(input('Enter a decimal number: '))

print('Octal value: ', end='')
DecimalOctal(num)