class Solution:
    def get_min_max(self, arr):
        if not arr:
            return None,None
        mn=arr[0]
        mx=arr[0]
        for n in arr:
            if n>mx:
                mx=n
            if n<mn:
                mn=n
        return mn,mx
            
      
