# 12. write a recursive function for binary search

def binarySearchRecursive(arr, target, low, high):
    if l > h:
        return -1
    
    mid = (l + h) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binarySearchRecursive(arr, target, l, mid - 1)
    else:
        return binarySearchRecursive(arr, target, mid + 1, h)

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23
result = binarySearchRecursive(arr, target, 0, len(arr) - 1)
print(result)
