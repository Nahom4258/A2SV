class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        # count zeroes for the rows & cols
        col_length = len(grid[0])
        row_length = len(grid)
        
        _dict = {
            'row': [0] * len(grid),
            'col': [0] * len(grid[0])
        }
        
        for r, row in enumerate(grid):
            for c, value in enumerate(row):
                if value == 0:
                    _dict['row'][r] += 1
                    _dict['col'][c] += 1
                    
        answer = []
        for r, row in enumerate(grid):
            my_row = []
            for c, value in enumerate(row):
                ans = (row_length - _dict['row'][r]) + (col_length - _dict['col'][c]) - _dict['row'][r] - _dict['col'][c]
                my_row.append(ans)
            answer.append(my_row)
            
        return answer
                
                
                
                