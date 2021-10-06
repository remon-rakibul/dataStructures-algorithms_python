def binary_search_itr(arr, key):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            r = mid - 1
        elif key > arr[mid]:
            l = mid + 1
    return -1


a = [4, 11, 18, 30, 54]
found = binary_search_itr(a, 54)
print('Result:', found)
