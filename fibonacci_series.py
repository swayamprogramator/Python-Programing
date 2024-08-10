num = int(input('Enter number of terms: '))
a, b = 0, 1
if(num>=1):
    print('The Fibonacci series: ')  
    print(a,end=' ')
    print(b,end=' ')
    for i in range (2, num):
        c = a + b
        print(c, end=' ')
        a = b
        b = c