def OctalDecimal(num):  #user-defined function
    decimal = 0
    base = 1  #Initializing base value to 1, i.e 8^0 

    while (num):
        # Extracting last digit
        last_digit = num % 10
        num = int(num / 10)

        decimal += last_digit * base
        base = base * 8

    return decimal

# take inputs
num = int(input('Enter an octal number: '))

# calling function and display result
print('The decimal value is =',OctalDecimal(num))