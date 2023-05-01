class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        visited = set()
        ans = [[0 for i in range(len(mat[0]))] for i in range(len(mat))]
        dist = 0
        checker = False
        def check(row,col):
            return True if row < len(mat) and row >= 0 and col < len(mat[0]) and col >= 0 else False
        def bfs():
            nonlocal queue,dist,ans
            directions = [[-1,0],[0,1],[1,0],[0,-1]]
            for row in range(len(mat)):
                for col in range(len(mat[0])):
                    if mat[row][col] == 0:
                        queue.append((row,col))
                        visited.add((row,col))
            while queue:
                length = len(queue)
                for i in range(length):
                    row,col = queue.popleft()
                    if mat[row][col] == 1:
                        ans[row][col] = dist
                    for direction in directions:
                        new_row = row + direction[0]
                        new_col = col + direction[1]
                        if check(new_row,new_col) and (new_row,new_col) not in visited:
                            queue.append((new_row,new_col))
                            visited.add((new_row,new_col))
                dist += 1
                            # ans[new_row][new_col] = dist
            return ans
            
        return bfs()