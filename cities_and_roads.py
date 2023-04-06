cities = int(input())

graph = []

for row in range(cities):
    graph.append(list(map(int, input().split())))
    
count = 0

for row in graph:
    count += row.count(1)
    
print(int(count/2))