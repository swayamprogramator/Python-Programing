l = [75, 110, 111, 119, 32, 80, 114, 111, 103, 114, 97, 109]
print("List of ASCII value =", l)

string = ""
for num in l:
    string = string + chr(num)
  
print ("String:", str(string))