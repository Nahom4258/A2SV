class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row_n = len(dungeon)
        col_n = len(dungeon[0])

        for row in range(row_n-1, -1, -1):
            for col in range(col_n-1, -1, -1):
                curr = dungeon[row][col]
                
                if row == row_n-1 and col == col_n-1:
                    dungeon[row][col] = min(0, dungeon[row][col])
                elif row == row_n-1:
                    dungeon[row][col] = min(0, dungeon[row][col]+dungeon[row][col+1])
                elif col == col_n-1:
                    dungeon[row][col] = min(0, dungeon[row][col]+dungeon[row+1][col])
                else:
                    dungeon[row][col] = min(0, dungeon[row][col] + max(dungeon[row][col+1], dungeon[row+1][col]))

        return abs(dungeon[0][0])+1