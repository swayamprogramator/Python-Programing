my_list = ['@know*', 'pr#ogra!m^', '(py_th@on_3}']

# initializing special characters
special_char = '@_!#$%^&*()<>?/\|}{~:;.[]'
 
# using join() + generator to remove special characters
out_list = [''.join(x for x in string if not x in special_char) for string in my_list]
 
# print list without special characters
print('List after removal of special characters:', out_list)