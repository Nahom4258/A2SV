class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        def check(row,col):
            return True if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]) else False
        def bfs():
            visited = set([(0,0)])
            queue = deque([(0,0,1)])
            directions = [[0,-1],[0,1],[-1,-1],[-1,0],[-1,1],[1,-1],[1,0],[1,1]]

            while queue:
                row,col,dist = queue.popleft()
                if row == len(grid)-1 and col == len(grid[0])-1:
                    return dist
                for direction in directions:
                    new_col = col+direction[1]
                    new_row = row+direction[0]
                    if check(row + direction[0],col+direction[1]):
                        if (new_row,new_col) not in visited and grid[new_row][new_col] == 0:
                            visited.add((new_row,new_col))
                            queue.append((new_row,new_col,dist+1))
            return -1
        return bfs()