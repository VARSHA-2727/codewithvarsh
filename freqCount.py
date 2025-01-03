class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr):
        n=len(arr)
        freq=[0]*(n+1)
        for n in arr:
            freq[n]+=1
        return freq[1:]



