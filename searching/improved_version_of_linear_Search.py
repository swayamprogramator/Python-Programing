def linearSearch(arr, key): 
    n = len(arr)
    i = 0
    j = n-1
    while(i <= n/2):
        if(key == arr[i]):
            return i
        elif(key == arr[j]):
            return j
        else:
            i = i+1
            j = j-1
    return -1

arr = [50, 90, 30, 70, 60] 
key = int(input('Enter number to search: '))  

index = linearSearch(arr, key) 

# display result
if (index == -1):
    print(key, 'not Found.')
else:
    print(key, 'Found at Index', index)
