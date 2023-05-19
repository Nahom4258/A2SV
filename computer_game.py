t = int(input())
 
for _ in range(t):
    grid = []
    
    max_col = int(input())
    
    for __ in range(2):
        grid.append(list(map(int, list(input()))))
    
    visited = set()
    possible = [False]
    # direction=  right,    left,   down,     up  , up_left, up_right, down_left, down_right
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    def dfs(row, col):
        if row == 1 and col == max_col-1:
            possible[0] = True
            return
        visited.add((row, col))
        
        for direction in directions:
            new_row = row + direction[0]
            new_col = col + direction[1]
            
            if 0 <= new_row < 2 and 0 <= new_col < max_col and grid[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                dfs(new_row, new_col)
                
    dfs(0, 0)
    
    print('YES' if possible[0] else 'NO')