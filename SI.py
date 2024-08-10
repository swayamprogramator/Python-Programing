P = float(input('Enter principal amount: '))
R = float(input('Enter the interest rate: '))
T = float(input('Enter time: '))


SI = (P * R * T) / 100


print('Simple interest = ',SI )
print('Total amount = ',( P + SI ))