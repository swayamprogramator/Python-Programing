def BinarySearch(arr, low, high, key):  #user-defined function
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

arr = [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 ]  #array
key = 40  #search key

# calling function
result = BinarySearch(arr, 0, len(arr)-1, key)

# display result
if result != -1:
    print(key, "Found at index", str(result))
else:
    print(key, "not Found")