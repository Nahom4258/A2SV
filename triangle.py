class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = dict()

        for i in range(len(triangle)-1, -1, -1):
            for j in range(len(triangle[i])):
                if i == len(triangle)-1:
                    memo[(i, j)] = triangle[i][j]
                else:
                    memo[(i, j)] = triangle[i][j] + min(memo[(i+1, j)], memo[(i+1, j+1)])

        # print('mem: ', memo)

        return memo[(0, 0)]