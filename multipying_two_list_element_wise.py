list1 = [5,6,4,3]
list2 = [3,5,3,3]

print("List1:", str(list1))
print("List2:", str(list2))

result = []
for i in range(0, len(list1)):
   result.append(list1[i] * list2[i])

print("Product:", str(result))