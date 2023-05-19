from collections import defaultdict
from collections import deque
 
n, m = map(int, input().split(' '))
 
gold = list(map(int, input().split(' ')))
 
graph = defaultdict(list)
 
for _ in range(m):
    a, b = map(int, input().split(' '))    
    graph[a].append(b)
    graph[b].append(a)
    
visited = set()
val = 0
 
for i in range(1, n+1):    
    minim = float('inf')
    if i not in visited:
        
        vis = set([i])
        queue = deque([i])
        
        while queue:
            length = len(queue)
            
            for _ in range(length):
                key = queue.popleft()
                
                minim = min(minim, gold[key-1])
                
                for n in graph[key]:
                    if n not in visited and n not in vis:
                        vis.add(n)
                        queue.append(n)
                        visited.add(n)
                        
        val += minim
    
print(val)