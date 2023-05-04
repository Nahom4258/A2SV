class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        side = defaultdict(list)

        for edge in edges:
            left, right = edge
            graph[left].append(right)
            graph[right].append(left)

        def dfs(head, parent):
            counter = 0

            for neighbour in graph[head]:
                if neighbour == parent:
                    continue
                counter_deep = dfs(neighbour, head)

                if counter_deep > 0 or hasApple[neighbour]:
                    counter += (2+counter_deep)

            return counter

        return dfs(0, -1)