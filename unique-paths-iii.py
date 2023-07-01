class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        row_len = len(grid)
        col_len = len(grid[0])
        start = (0, 0)
        end = (0, 0)
        free_space = 0
        ans = 0

        def is_valid(row, col):
            return 0 <= row < row_len and 0 <= col < col_len

        for i in range(row_len):
            for j in range(col_len):
                # get starting coordinate
                if grid[i][j] == 1:
                    start = (i, j)

                # get ending coordinate
                if grid[i][j] == 2:
                    end = (i, j)

                # count empty squares
                if grid[i][j] == 0:
                    free_space += 1

        # print('enddd: ', end)

        def dfs(row, col, visited):
            # print('r, c: ', row, col)
            if grid[row][col] == 2:
                # print('foundddd')
                nonlocal ans
                if len(visited) == free_space+1:
                    ans += 1

                return

            for d in directions:
                new_r, new_c = row+d[0], col+d[1]

                if is_valid(new_r, new_c) and (grid[new_r][new_c] == 0 or grid[new_r][new_c] == 2) and (new_r, new_c) not in visited:
                    visited.add((new_r, new_c))
                    dfs(new_r, new_c, visited)
                    visited.remove((new_r, new_c))


            return

        dfs(start[0], start[1], set())

        return ans