class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for pre in prerequisites:
            a, b = pre

            graph[b].append(a)
            indegree[a] += 1
        
        ans = 0
        queue = deque()

        for i in range(numCourses):
            if not indegree[i]:
                queue.append(i)

        while queue:
            length = len(queue)

            for _ in range(length):
                curr = queue.popleft()

                ans += 1

                for child in graph[curr]:
                    indegree[child] -= 1

                    if not indegree[child]:
                        queue.append(child)

        return ans == numCourses