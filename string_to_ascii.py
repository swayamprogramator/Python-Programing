string = input("Enter any string: ")

# printing ascii value of each character
for i in range(len(string)):
    print(f'The ASCII value of character {string[i]} = {ord(string[i])}')