def ComputeSum(num): #user-defined function
    sum = 0
    while (num != 0):  
        sum += (num % 10) 
        num //= 10
        
    return sum


num = int(input('Enter a number: '))

print('Sum of digits in number =', ComputeSum(num))