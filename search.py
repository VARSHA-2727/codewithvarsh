def search(arr):
    if key not in arr:
        return -1
    for i in range(len(arr)):
        if arr[i]==key:
            return i
arr=[1,4,5,7]
key=4
result=search(arr)
print(result)
