from collections import defaultdict

vertex_no = int(input())

operations_no = int(input())

graph = defaultdict(list)

for _ in range(operations_no):
    op = list(map(int, input().split()))
    
    # if operation == 1 - AddEdge(u, v) if 2 - Vertex(u)
    if op[0] == 1:
        graph[op[1]].append(op[2])
        graph[op[2]].append(op[1])
    
    elif op[0] == 2:
        print(*graph[op[1]])