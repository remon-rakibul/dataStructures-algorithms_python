def linear_search(arr, key):
    index = 0
    while index < len(arr):
        if arr[index] == key:
            return index
        index += 1
    return -1


a = [12, 13, 4, 5, 6]
found = linear_search(a, 4)
print('Result:', found)
