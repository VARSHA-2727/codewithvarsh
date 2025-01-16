def third_largest(arr):
    n=len(arr)
    if n<3:
        return None
    arr.sort(reverse=True)
    return arr[2]
arr=[2,4,3,6,7]
result=third_largest(arr)
print(result)
