a = [20, 25, 30, 40, 55, 15]
b = [10, 35, 30, 26, 67, 12]

print('list1 =', a)
print('list2 =', b)

# subtraction of element using zip
sub = [x-y for (x, y) in zip(a, b)]

print('list1 - list2 =', sub)