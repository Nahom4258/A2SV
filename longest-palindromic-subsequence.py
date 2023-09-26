class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        memo = [[0 for _ in range(n)] for _ in range(n)]

        def is_valid(r, c):
            if 0 <= r < n and 0 <= c < n:
                return memo[r][c]

            return 0

        s2 = s[::-1]
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s[i] == s2[j]:
                    memo[i][j] = 1 + is_valid(i+1, j+1)
                else:
                    memo[i][j] = max(is_valid(i+1, j), is_valid(i, j+1))

        return memo[0][0]