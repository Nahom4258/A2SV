class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for x in range(n)] for y in range(n)]
        number = 1

        limit = n
        while limit >= 0:
            top = n-limit
            right = n - limit
            bottom = limit - 1
            left = limit - 1

            while top < limit:
                ans[right][top] = number
                number += 1
                top += 1
            top -= 1
            right += 1
            while right < limit:
                ans[right][top] = number
                number += 1
                right += 1
            bottom -= 1

            while bottom >= n-limit:
                ans[left][bottom] = number
                number += 1
                bottom -= 1
            bottom += 1
            left -= 1

            while left >= n-limit+1:
                ans[left][bottom] = number
                number += 1
                left -= 1

            limit -= 1

        return ans