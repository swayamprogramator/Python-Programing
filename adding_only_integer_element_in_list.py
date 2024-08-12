def sum_list(list):
    return sum([int(i) for i in list if type(i) == int or i.isdigit()])

l1 = [5, 'know', 8, 'program']
l2 = ['python', 7, 'code']

print(sum_list(l1))
print(sum_list(l2))