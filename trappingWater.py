
class Solution:
    def maxWater(self, arr):
        length=len(arr)
        left=[0]*length
        right=[0]*length
        trapped=0
        left[0]=arr[0]
        right[-1]=arr[-1]
        for i in range(1,len(arr)):
            left[i]=max(left[i-1],arr[i])
        for i in range (length-2,-1,-1):
            right[i]=max(right[i+1],arr[i])
        for i in range(length):
            trapped+=min(left[i],right[i])-arr[i]
        return trapped
            
        


#{ 
 # Driver Code Starts
#Initial template for Python 3

import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
