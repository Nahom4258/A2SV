class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []
        n = min([len(x) for x in strs])

        for i in range(n):
            ch = ''
            not_same = False
            for j in range(len(strs)):
                if ch == '':
                    ch = strs[j][i]
                elif strs[j][i] != ch:
                    not_same = True
                    break

            if not_same:
                break
            else:
                ans.append(ch)

        return ''.join(ans)