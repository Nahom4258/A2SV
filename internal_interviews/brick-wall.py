class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        ending_col = defaultdict(int)

        for i in range(len(wall)):
            start = 0
            for j in range(len(wall[i])-1):
                start += wall[i][j]
                ending_col[start] += 1

        return len(wall) - max(ending_col.values(), default=0)