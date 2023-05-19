from collections import deque
 
x, y, fx, fy = map(int, input().split())
 
allowed = set()
 
for _ in range(int(input())):
    r, c1, c2 = map(int, input().split())
    
    for i in range(c1, c2 +1):
        allowed.add((r, i))
    
queue = deque([(x, y)])
visited =set([(x, y)])
 
isValid = lambda r, c: 0 < r <= 10 ** 9 and 0 < c <= 10 ** 9
directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1,-1), (-1, 1), (1, -1), (1, 1)]
 
ans = 0
 
cont = True
 
while queue and cont:
    l = len(queue)
    
    for _ in range(l):
        x, y = queue.popleft()
        
        if (x, y) == (fx, fy):
            print(ans)
            cont = False
            break
        
        for r, c in directions:
            nx, ny = x + r, y + c
            
            # print(nx, ny, end=" after ")
            
            if isValid(nx, ny) and (nx, ny) not in visited and (nx, ny) in allowed:
                queue.append((nx, ny))
                visited.add((nx, ny))
    
    ans += 1
 
if cont:
    print(-1)