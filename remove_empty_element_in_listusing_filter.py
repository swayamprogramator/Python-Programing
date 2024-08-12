my_list = ['Know Program', '', 'Python', 'C', '', 'Java']

print('List:', my_list)

# remove empty string using filter()
new_list = list(filter(None, my_list))

print('New List:', new_list)

