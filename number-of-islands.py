class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        def valid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(row, col):
            visited.add((row, col))

            for d in directions:
                new_r, new_c = row+d[0], col+d[1]

                if valid(new_r, new_c) and grid[new_r][new_c] == "1" and (new_r, new_c) not in visited:
                    dfs(new_r, new_c)

            return

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    ans += 1
                    dfs(i, j)

        return ans