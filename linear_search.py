def linear_search(arr,length,item):
    for i in range(0,length):
        if arr[i]==item:
            return i
    return -1
arr=[10,20,30,40,5]
item=int(input('enter the val '))
length=len(arr)
result=linear_search(arr,length,item)
if result==-1:
    print(f'{item} not found')
else:
    print(f'{item} found in index {result}')
