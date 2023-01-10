class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        answer = []
        queens = set(map(tuple, queens))
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,1), (1,0), (1,-1)]

        for direction in directions:
            rowK, colK = king[0], king[1]
            while (0 <= rowK < 8) and (0 <= colK < 8):
                if (rowK, colK) in queens:
                    answer.append([rowK, colK])
                    break

                rowK += direction[0]
                colK += direction[1]

        return answer
                
                
        
        
        
        
    