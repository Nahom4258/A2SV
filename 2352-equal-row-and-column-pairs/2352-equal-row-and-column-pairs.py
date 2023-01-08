class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter = 0
        columns = [] 
        
        for i in range(len(grid[0])):
            new_col = []
            for j in range(len(grid)):
                new_col.append(grid[j][i])
            columns.append(new_col)
            
        print(columns)
        for row in grid:
            if row in columns:
                counter += columns.count(row)
                
        return counter