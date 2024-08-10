p= 1000
r = 10
t = 5
n = 6

r = r/100
a = p * pow( 1+(r/n), n*t)
ci = a - p

print('Compound interest = %.2f' %ci)
print('Total amount = %.2f' %a)