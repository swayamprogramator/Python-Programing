list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 7, 8]

list = []

for item in list1:
   for item1 in list2:
      if item == item1:
         list.append(item)

print(list)