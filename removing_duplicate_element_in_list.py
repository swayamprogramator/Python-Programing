my_list = [1, 2, 3, 1, 5, 3, 4, 2, 7]

print('List:', my_list)

# removed duplicates item using native method
new_list = []
for i in my_list:
    if i not in new_list:
        new_list.append(i)

print('New list:', new_list)