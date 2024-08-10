num = int(input('Display multiplication table of: '))

# print multiplication table
for i in range(1, 11):
    print ("%d * %d = %d" % (num, i, num * i))