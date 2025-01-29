class Solution:
    def find(self, arr, x):
        f_o=None
        l_o=None
        if not arr:
            return None
            for i in range(len(arr)):
                if arr[i]==x:
                    if f_o is None:
                        f_o = i
                    l_o = i
            if f_o is None:
                return None
            return f_o,l_o
        
        # code here
