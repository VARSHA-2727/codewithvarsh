class Solution:
    def removeDuplicates(self, arr):
        n = len(arr)
        if n == 0 or n == 1:  # Handle edge cases
            return n
        
        j = 0  # Pointer for distinct elements
        
        for i in range(1, n):  # Loop through the array
            if arr[i] != arr[j]:  # If a distinct element is found
                j += 1
                arr[j] = arr[i]  # Move distinct element to the front

        return j + 1  # Return size of modified array



#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    t = int(data[0])
    line = 1

    solution = Solution()

    for _ in range(t):
        if line < len(data):
            arr = list(map(int, data[line].split()))
            line += 1
            ans = solution.removeDuplicates(arr)
            for i in range(ans):
                print(arr[i], end=" ")
            print()
        print("~")
