def find_reapted_value(arr):
    reapted_value=[]
    for i in range( len(arr)):
        if arr[i] in arr[:i] and arr[i] not in reapted_value :
            reapted_value.append(arr[i])
    return reapted_value
arr=[1, 2, 2, 4, 4, 6, 7]
result=find_reapted_value(arr)
print(result)
    
