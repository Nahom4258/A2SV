class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        memo = defaultdict(int)
        memo[(0, 0)] = poured

        for i in range(query_row+1):
            for j in range(i+1):
                if memo[(i, j)] > 1:
                    left_over = memo[(i, j)] - 1
                    memo[(i, j)] -= left_over
                    # add to left
                    memo[(i+1, j)] += left_over/2
                    # add to right
                    memo[(i+1, j+1)] += left_over/2
                    
        # print('ans: ', memo)

        return memo[(query_row, query_glass)]