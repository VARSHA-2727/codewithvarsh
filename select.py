def sort(arr):
    n=len(arr)
    for i in range(0,n):
        min_index=i
        for j in range(i+1,n):
            if arr[min_index]>arr[j]:
                min_index=j
        temp=arr[min_index]
        arr[min_index]=arr[i]
        arr[i]=temp
    return arr
    
arr=[32,12,45,23]
sorted_arr=sort(arr)
print(sorted_arr)
