class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        p = Counter(p)
        curr = list(s[:k])
        ans = []
        
        if Counter(curr) == p:
            ans.append(0)
        
        for i in range(k, len(s)):
            curr.append(s[i])
            del curr[0]
            if Counter(curr) == p:
                ans.append(i - k + 1)
        
        return ans