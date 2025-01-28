class Solution:
    def minRow(self,a):
        min_count = float('inf')
        min_row = 1
        for i in range(len(mat)):
            count = sum(mat[i])
            if count < min_count:
                min_count = count
                min_row = i + 1
        return min_row
