class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n = numCourses
        path = [[False]*n for _ in range(n)]

        # fill node with itself
        for i in range(n):
            path[i][i] = True
        
        # fill path from prereq
        for s, e in prerequisites:
            path[s][e] = True

        for k in range(n):
            for j in range(n):
                for i in range(n):
                    path[i][j] = path[i][j] or (path[i][k] and path[k][j])

        ans = []
        for s, e in queries:
            ans.append(path[s][e])

        return ans