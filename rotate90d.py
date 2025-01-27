
class Solution:
    
    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self, mat): 
        mat_c=[row[:]for row in mat]
        if not mat:
            return False
            for i in range(n):
                for j in range(i,n):
                    mat[i][j],mat[j][i]==mat[j][i],mat[i][j]
                    
                for row in mat_c:
                    row.reverse()
            return mat_c
