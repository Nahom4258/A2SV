class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ans = []

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                ans.append(matrix[row][col])

        return sorted(ans)[k-1]