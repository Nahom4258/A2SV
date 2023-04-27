class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1,0), (0, -1), (0,1)]
        visited = set()
        max_area = 0

        def dfs(row, col):
            if grid[row][col] == 0:
                return 0

            visited.add((row, col))
            count = 0

            for direction in directions:
                newRow, newCol = row + direction[0], col + direction[1]
                
                if newRow >= 0 and newRow < len(grid) and newCol >= 0 and newCol < len(grid[0]):
                    if (newRow, newCol) not in visited:
                        count += dfs(newRow, newCol)

            return count + 1

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if str(row)+str(col) not in visited and grid[row][col] == 1:
                    # print('rc: ', row, col)
                    max_area = max(max_area, dfs(row, col))
        # print('ans: ', dfs(3, 8))

        return max_area