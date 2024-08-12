my_list = [1, 2, 3, 1, 4, 3, 5, 2, 7]

print('List:', my_list)

# removed duplicates item using list comprehension
new_list = []
[new_list.append(x) for x in my_list if x not in new_list]

print('New list:', new_list)