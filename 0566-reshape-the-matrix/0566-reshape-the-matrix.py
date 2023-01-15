class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if (len(mat[0]) * len(mat)) == (r * c):
            ans = []
            unique = 0
            
            for row in range(r):
                temp = []
                for col in range(c):
                    mat_row = unique // len(mat[0])
                    mat_col = unique % len(mat[0])
                    temp.append(mat[mat_row][mat_col])
                    unique += 1
                    
                ans.append(temp)
                
            return ans
        
        return mat