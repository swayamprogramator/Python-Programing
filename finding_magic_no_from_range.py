print("Enter a range")
i1 = int(input("Start: "))
i2 = int(input("Last: "))

print("Magic numbers between ",i1," and ",i2," are: ")
for i in range(i1,i2+1):
   if (i % 9 == 1):
      print(i)