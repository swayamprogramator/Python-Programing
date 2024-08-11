n = float(input('How many numbers: '))

total_sum = 0

i =1
while i <= n:
    num = float(input('Enter number: '))
    total_sum += num
    
    i = i+1

avg = total_sum / n

print('The average of numbers = %0.2f' %avg)