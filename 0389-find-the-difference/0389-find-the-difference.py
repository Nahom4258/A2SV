class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        ans = ''
        
        for i in range(len(t)):
            if i == len(t) - 1:
                ans = t[len(t) - 1]
                break
            
            if s[i] != t[i]:
                ans = t[i]
                break
                
        return ans