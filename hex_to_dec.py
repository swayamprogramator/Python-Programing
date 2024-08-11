def DecimalHexa(n):  #user-defined function
    hexa = ['0'] * 100
    i = 0
    while(n != 0):

        rem = 0
        rem = n % 16

        if(rem < 10): 
            hexa[i] = chr(rem + 48)
            i = i + 1
        else: 
            hexa[i] = chr(rem + 55)
            i = i + 1
        n = int(n / 16)

    #print hexa number array in reverse order
    j = i - 1
    while(j >= 0): 
        print((hexa[j]), end = ''); 
        j = j - 1

# take inputs
num = int(input('Enter a decimal number: '))

# calling function and display result
print('HexaDecimal value = ', end = '')
DecimalHexa(num)