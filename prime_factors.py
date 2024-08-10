num = int(input('Enter number: '))
for i in range(2, num + 1):
    if(num % i == 0):
        isPrime = 1
        for j in range(2, (i //2 + 1)):
            if(i % j == 0):
                isPrime = 0
                break
        if (isPrime == 1):
            print(i,end=' ')
print('are the prime factors of number',num)