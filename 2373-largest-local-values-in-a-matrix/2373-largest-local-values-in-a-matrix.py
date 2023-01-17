class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        maxLocal = []
        for row in range(len(grid) - 2):
            temp = []
            for col in range(len(grid[2]) - 2):
                temp.append(max(grid[row][col], grid[row][col + 1], grid[row][col + 2], grid[row + 1][col], grid[row + 1][col + 1], grid[row + 1][col + 2], grid[row + 2][col], grid[row + 2][col + 1], grid[row + 2][col + 2]))
                
            maxLocal.append(temp)
            
        return maxLocal