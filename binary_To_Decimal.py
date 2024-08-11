
def BinaryDecimal(n):  #user-defined function
    num, dec, base = n, 0, 1
     
    temp = num
    while(temp):
        digit = temp % 10
        temp = int(temp / 10)
        
        dec += digit * base
        base = base * 2
    return dec
 
num = int(input('Enter a binary number: '))

print('The decimal value is =', BinaryDecimal(num))