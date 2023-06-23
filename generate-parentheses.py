class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        memo = set()

        def backtrack(open, close, string, ans):
            if open <= 0 and close <= 0:
                # print('op: {}, cl: {}'.format(open, close))
                # print('val: ', string)
                ans.append(''.join(string))
                return

            temp_open, temp_close = open, close
            while temp_open or temp_close:
                open_add = ''.join(string+['('])
                close_add = ''.join(string+[')'])
                if temp_open and temp_open <= temp_close and open_add not in memo:
                    backtrack(open-1, close, string+['('], ans)
                    memo.add(open_add)
                    temp_open -= 1
                elif temp_close and temp_close > temp_open and close_add not in memo:
                    backtrack(open, close-1, string+[')'], ans)
                    memo.add(close_add)
                    temp_close -= 1
                else:
                    return

            return

        ans = []

        backtrack(n, n, [], ans)

        return ans