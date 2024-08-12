my_list = ['Know Program', '', 'Python', 'C', '', 'Java']

print('List:', my_list)

# remove empty string using native method
new_list = []
for i in my_list:
    if (i):
        new_list.append(i)

print('New List:', new_list)