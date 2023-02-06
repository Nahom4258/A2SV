from collections import defaultdict
 
 
t = int(input())
 
for _ in range(t):
    temp = list(map(int, input().split()))
    n = temp[0]
    m = temp[1]
    
    board = []
    for __ in range(n):
        board.append(list(map(int, input().split())))
        
    left_diag = defaultdict(int)
    right_diag = defaultdict(int)
    
    for row in range(n):
        for col in range(m):
            left_diag[str(row + col)] += board[row][col]
            right_diag[str(row - col)] += board[row][col]
            
    maxim = 0
    for row in range(n):
        for col in range(m):
            sum = 0
            sum += right_diag[str(row - col)]
            sum += left_diag[str(row + col)]
            sum -= board[row][col]
            
            maxim = max(sum, maxim)
            
    print(maxim)
