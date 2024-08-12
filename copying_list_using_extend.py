def clone(list1):
   list_copy = []
   list_copy.extend(list1)
   return list_copy

list1 = [1,2,3]
list2 = clone(list1)
print("List1:", list1)
print("List2:", list2)