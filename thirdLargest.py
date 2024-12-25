class Solution:
    def thirdLargest(self,arr,n):
        if n < 3:
            return -1  # No third largest element possible

        # Initialize the three largest elements
        largest = float('-inf')
        slarge = float('-inf')
        tlarge = float('-inf')

        # Traverse the array
        for i in range(n):
            if arr[i] > largest:  # Update largest
                tlarge = slarge
                slarge = largest
                largest = arr[i]
            elif arr[i] > slarge:  # Update second largest
                tlarge = slarge
                slarge = arr[i]
            elif arr[i] > tlarge:  # Update third largest
                tlarge = arr[i]

        # Return the third largest element
        return tlarge
            


#{ 
 # Driver Code Starts
# Your code goes here
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split()))
        print(Solution().thirdLargest(arr))
        print("~")
