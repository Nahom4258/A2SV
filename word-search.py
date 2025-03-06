class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirns = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        l_r, l_c = len(board), len(board[0])

        def valid(i, j):
            return 0 <= i < l_r and 0 <= j < l_c

        def helper(i, j, vis, s_idx):
            if s_idx >= len(word):
                return False

            if word[s_idx] != board[i][j]:
                return False

            if s_idx == len(word)-1 and word[s_idx] == board[i][j]:
                return True

            ans = False
            for d in dirns:
                new_r, new_c = i+d[0], j+d[1]

                if (new_r, new_c) not in vis and valid(new_r, new_c):
                    vis.add((new_r, new_c))
                    ans = ans or helper(new_r, new_c, vis, s_idx+1)
                    vis.remove((new_r, new_c))

            return ans

        for i in range(l_r):
            for j in range(l_c):
                if board[i][j] == word[0]:
                    ans = helper(i, j, set([(i, j)]), 0)
                    if ans:
                        return ans

        return False