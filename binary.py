def binary_search(l,key):
    l=sorted(l)
    if len(l)==0:
        return False
    mid=len(l)//2
    if l[mid]==key:
        return True
    elif key<l[mid]:
        return binary_search(l[:mid],key)
    else:
       return binary_search(l[mid+1:],key)
l=[10,20,30,40,20,36]
key=30
result=binary_search(l,key)
print(result)
print(l)
    
        
    
