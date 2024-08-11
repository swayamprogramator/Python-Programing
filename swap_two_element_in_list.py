def swap(l, p1, p2):
   l[p1], l[p2] = l[p2], l[p1]
   return l

l = [5, 6, 7, 8, 9]

print("List:", l)

# take swap position of elements
p1 = int(input("Enter Position 1 Element: "))
p2 = int(input("Enter Position 2 Element: "))

print("New List:", swap(l, p1-1, p2-1))