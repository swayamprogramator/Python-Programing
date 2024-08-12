def compare(list1,list2):
   list1.sort()
   list2.sort()
   if(list1==list2):
      return "Equal"
   else:
      return "Non equal"
l1=[1,2,3]
l2=[2,1,3]
print("Comparision using 'list.sort()' comparison:-",compare(l1,l2))
l3=[1,2,3]
l4=[1,3,2]
print("Comparison using '==' operator:-",compare(l3,l4))