class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        answer  = []
        reverse = False
        
        for i in range(len(mat)):
            # do action here
            temp = []
            row = i
            col = 0
            while row >= 0 and col < len(mat[0]):
                temp.append(mat[row][col])
                row -= 1
                col += 1
            if reverse:
                answer += temp[::-1]
            else:
                answer += temp
            reverse = not reverse
        
        if len(mat[0]) > 1:
            for i in range(1, len(mat[0])):
                # action here
                temp = []
                row = len(mat) - 1
                col = i
                while col < len(mat[0]) and row >= 0:
                    temp.append(mat[row][col])
                    row -= 1
                    col += 1
                    
                if reverse:
                    answer += temp[::-1]
                else:
                    answer += temp
                reverse = not reverse
            
        return answer
                
                
                