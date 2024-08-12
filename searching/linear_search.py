def linearSearch(arr, key): 
    for i in range(len(arr)): 
        if (arr[i] == key): 
            return i 
    return -1

arr = [50, 90, 30, 70, 60]  
key = 70 

index = linearSearch(arr, key)

# display result
if (index == -1):
    print(key, 'not Found.')
else:
    print(key, 'Found at Index', index)