class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for a, b in prerequisites:
            graph[a].append(b)

        def is_prereq(a, target, visited):
            visited.add(a)
            if a == target:
                return True

            ret = False
            for child in graph[a]:
                if child not in visited:
                    ret = ret or is_prereq(child, target, visited)

            return ret

        ans = []
        for a, b in queries:
            ans.append(is_prereq(a, b, set()))

        return ans