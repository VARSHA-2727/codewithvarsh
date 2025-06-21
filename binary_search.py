def binary_search(arr, key,n):
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == key:
            return mid  # Found: return index
        elif arr[mid] < key:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return -1  # Not found
arr=[10,20,30,40]
n=len(arr)
key=int(input('enter the num'))
result=binary_search(arr,key,n)
if result!=-1:
    print(f'key  found at {result}')
else:
    print( 'key not found ')


