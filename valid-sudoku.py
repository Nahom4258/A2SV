class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    temp = board[row][col]
                    board[row][col] = 'temp'
                    for i in range(9):
                        if board[i][col] == temp or board[row][i] == temp:
                            return False

                    start_of_row = (row//3) * 3
                    start_of_col = (col//3) * 3
                    for r in range(start_of_row, start_of_row+3):
                        for c in range(start_of_col, start_of_col+3):
                            if board[r][c] == temp:
                                return False

                    board[row][col] = temp

        return True