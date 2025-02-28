class Solution:
    def maxWater(self, arr):
        left,right=0,len(arr)-1
        most_water_area=0
        while(left<right):
            length=min(arr[left],arr[right])
            width=right-left
            most_water_area=max(most_water_area,length*width)
            if arr[left]<arr[right]:
                left+=1
            else:
                right-=1
        return  most_water_area 
        
