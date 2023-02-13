class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        maxim = 0
        
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[j] == s[i]:
                    maxim = max(maxim, j)
                    
            if maxim == i:
                res.append(maxim + 1)
                maxim = i + 1

        ans = [res[0]]

        for i in range(1, len(res)):
            ans.append(res[i] - res[i - 1])

        return ans