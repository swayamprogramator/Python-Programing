num = int(input('Enter any number: '))

# count number of digits
count = 0
while (num>0):
    num = num//10
    count = count+1
    
# printing number of digits
print('Number of digits:', count)