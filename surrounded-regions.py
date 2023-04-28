class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        max_row, max_col = len(board), len(board[0])

        def dfs(row, col):
            visited.add((row, col))
            print('r:', row, 'c:', col)

            for direction in directions:
                new_row, new_col = row+direction[0], col+direction[1]
                if 0 <= new_row < max_row and 0 <= new_col < max_col and (new_row, new_col) not in visited and board[new_row][new_col] == 'O':
                    dfs(new_row, new_col)

        for row in range(max_row):
            col_start, col_end = 0, max_col-1
            if board[row][col_start] == 'O' and board[row][col_start] not in visited:
                dfs(row, col_start)
            if board[row][col_end] == 'O' and board[row][col_end] not in visited:
                dfs(row, col_end)

        for col in range(max_col):
            row_start, row_end = 0, max_row-1
            if board[row_start][col] == 'O' and board[row_start][col] not in visited:
                dfs(row_start, col)
            if board[row_end][col] == 'O' and board[row_end][col] not in visited:
                dfs(row_end, col)

        # print('set: ', visited)
        for row in range(max_row):
            for col in range(max_col):
                if board[row][col] == 'O' and (row, col) not in visited:
                    board[row][col] = 'X'
        # dfs(3, 1)
        # print('set: ', visited)