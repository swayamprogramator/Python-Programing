def check_elements(l):
    #stores first element in a variable
    element = l[0]
    x = True
      
    # Comparing each element with first item 
    for i in l:
        if element != i:
            x = False
            break;
              
    if (x == True): 
        print("Yes, all elements are equal.")
    else: 
        print("No, all elements are not equal.")            


my_list = ['Know Program', 'Know Program', 'Know Program']
print('List:', my_list)
check_elements(my_list)