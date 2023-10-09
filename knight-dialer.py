class Solution:
    def knightDialer(self, n: int) -> int:
        directions = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
        keypad = [list('123'), list('456'), list('789'), list('*0#')]

        def valid(row, col):
            return 0 <= row < 4 and 0 <= col < 3

        memo = dict()
        def dfs(row, col, digit_count):
            if digit_count == 0:
               return 1

            ans = 0
            curr = keypad[row][col]
            for d in directions:
                new_r, new_c = row+d[0], col+d[1]
                if valid(new_r, new_c) and keypad[new_r][new_c].isdigit():
                    if (keypad[new_r][new_c], digit_count-1) in memo:
                        ans += memo[(keypad[new_r][new_c], digit_count-1)]
                    else:
                        ans += dfs(new_r, new_c, digit_count-1)

            memo[(curr, digit_count)] = ans

            return ans

        ans = 0
        for i in range(4):
            for j in range(3):
                if keypad[i][j].isdigit():
                    ans += dfs(i, j, n-1)

        return ans % (10**9 + 7)