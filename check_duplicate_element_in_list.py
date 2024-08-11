# take list
my_list = [1, 7, 8, 1, 5]

# printing original list
print('List:', my_list)

# check duplicates using count()
duplicate_item = {x for x in my_list if my_list.count(x) > 1}
if duplicate_item:
    print('Yes, the list contains duplicates.')
else:
    print('No, the list does not contains duplicates.')