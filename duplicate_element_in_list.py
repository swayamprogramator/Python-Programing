my_list = [1, 3, 7, 1, 2, 7, 5, 3, 8, 1]

# printing original list
print('List:', my_list)

# find duplicate items using count()
duplicate_item = {x for x in my_list if my_list.count(x) > 1}

# printing duplicate elements
print('Duplicate Elements:', duplicate_item)