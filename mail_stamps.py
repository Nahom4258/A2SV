from collections import (defaultdict, deque)
 
n = int(input())
 
graph = defaultdict(list)
 
for _ in range(n):
    left, right = map(int, input().split(' '))
    
    graph[left].append(right)
    graph[right].append(left)
    
node = None
for n in graph.keys():
    if len(graph[n]) == 1:
        node = n
        break
 
visited = set([node])
queue = deque([node])
path = [node]
 
while queue:
    length = len(queue)
    
    for _ in range(length):
        node = queue.popleft()
        for n in graph[node]:
            if n not in visited and n not in queue:
                visited.add(n)
                queue.append(n)
                path.append(n)
    
print(*path)