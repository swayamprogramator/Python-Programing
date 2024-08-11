num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

# choose the greater number
if (num1 > num2):
    greater = num1
else:
    greater = num2

while(True):
    # find LCM
    if(greater % num1 == 0 and greater % num2 == 0):
        print('The LCM of',num1,'and',num2,'is',greater)
        break
    greater += 1