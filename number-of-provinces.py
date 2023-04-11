class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        counter = 0
        visited = set()

        for row in range(len(isConnected)):
            for col in range(len(isConnected[0])):
                if isConnected[row][col]: 
                    graph[row+1]
                if isConnected[row][col] and row != col:
                    graph[row+1].append(col+1)

        def helper(vertex):
            visited.add(vertex)
            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    helper(neighbour)

        for i in range(len(isConnected)):
            if i+1 not in visited:
                counter += 1
                helper(i+1)

        return counter