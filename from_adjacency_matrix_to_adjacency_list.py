from collections import defaultdict

vertices = int(input())

graph = defaultdict(list)

for vertex in range(vertices):
    row = list(map(int, input().split()))
    
    for i in range(len(row)):
        if row[i] == 1:
            graph[vertex+1].append(i+1)
            
for key in graph:
    print(len(graph[key]), *graph[key])