my_list = ['Know Program', '', 'Python', 'C', '', 'Java']
print('List:', my_list)

# remove empty string using remove()
while('' in my_list):
    my_list.remove('')

print('New List:', my_list)