vertices = int(input())

graph = []
# sources if no edge comes INTO it
sources = []
# sinks if no edge comes OUT of it
sinks = []

for row in range(vertices):
    # find sinks from input
    curr_row = list(map(int, input().split()))
    if sum(curr_row) == 0:
        sinks.append(row + 1)
        
    graph.append(curr_row)
    
# find sources
for col in range(vertices):
    column = []
    for row in range(vertices):
        column.append(graph[row][col])
        
    if sum(column) == 0:
        sources.append(col + 1)
        
print(len(sources), *sources)
print(len(sinks), *sinks)