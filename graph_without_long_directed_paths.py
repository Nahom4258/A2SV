from collections import deque, defaultdict
 
v_no, e_no = map(int, input().split(' '))
 
graph = defaultdict(list)
nodes = set()
edges = []
 
for _ in range(e_no):
    a, b = map(int, input().split(' '))
    
    edges.append((a, b))
    graph[a].append(b)
    graph[b].append(a)
    nodes.add(a)
    nodes.add(b)
    
nodes = list(nodes)
nodes = [(x, None) for x in nodes]
 
found = True
# visited = set()
# def dfs(node, parent, boolean):
#     global found
#     global nodes
#     visited.add(node)
#     nodes[node-1] = (node, boolean)
    
#     for n in graph[node]:
#         if n not in visited:
#             dfs(n, node, not boolean)
#         elif n in visited and nodes[n-1][1] == nodes[node-1][1] and n != parent:
#             found = False
#             return
        
#     if not found:
#         return
    
# dfs(nodes[0][0], None, True)
 
visited = set([nodes[0][0]])
queue = deque([nodes[0][0]])
boolean = True
 
while queue and found:
    length = len(queue)
    for _ in range(length):
        # print('qu: ', queue)
        curr = queue.popleft()
        visited.add(curr)
        nodes[curr-1] = (curr, boolean)
        
        for n in graph[curr]:
            if n not in visited:
                queue.append(n)
                visited.add(n)
            elif n in visited and nodes[n-1][1] == nodes[curr-1][1] and n != curr:
                found = False
                break
        
    boolean = not boolean
 
# print('ed: ', nodes)
 
ans = []
if found:
    for u, v in edges:
        ans.append('0' if not nodes[u-1][1] else '1')
    print('YES')
    print(''.join(ans))
else:
    print('NO')
 
# print(nodes)