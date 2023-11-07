class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row_n, col_n = len(grid), len(grid[0])
        dirns = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def valid(row, col):
            return 0 <= row < row_n and 0 <= col < col_n and grid[row][col] == 1

        def dfs(row, col, visited):
            if not valid(row, col):
                return 1

            visited.add((row, col))

            ans = 0

            for d in dirns:
                new_r, new_c = row+d[0], col+d[1]

                if (new_r, new_c) not in visited:
                    ans += dfs(new_r, new_c, visited)

            return ans

        start = (0, 0)
        for i in range(row_n):
            for j in range(col_n):
                if grid[i][j] == 1:
                    start = (i, j)
                    break

        return dfs(start[0], start[1], set())