def BinarySearch(arr, low, high, key):  
    if high >= low:  #check base case
        mid = (high + low) // 2
        if (arr[mid] == key):
            return mid
        elif (arr[mid] > key):
            return BinarySearch(arr, low, mid - 1, key)
        else:
            return BinarySearch(arr, mid + 1, high, key)
    else:
        return -1

arr = [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 ]
key = 40  

result = BinarySearch(arr, 0, len(arr)-1, key)

if result != -1:
    print(key, "Found at index", str(result))
else:
    print(key, "not Found")