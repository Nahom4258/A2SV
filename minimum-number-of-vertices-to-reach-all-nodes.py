class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = []
        temp = set()

        for i in range(len(edges)):
            temp.add(edges[i][1])

        for i in range(n):
            if i not in temp:
                ans.append(i)

        return ans