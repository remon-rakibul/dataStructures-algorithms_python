def binary_search_rec(arr, key, l, r):
    if l > r:
        return -1
    else:
        mid = (l + r) // 2
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            return binary_search_rec(arr, key, l, mid-1)
        elif key > arr[mid]:
            return binary_search_rec(arr, key, mid+1, r)


a = [4, 11, 18, 30, 54]
found = binary_search_rec(a, 30, 0, len(a)-1)
print('Result:', found)
