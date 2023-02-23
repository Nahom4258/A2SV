class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = []
        k = len(s1)
        s1 = Counter(s1)
        curr = list(s2[:k])
        
        if Counter(curr) == s1:
            return True
        
        for i in range(k, len(s2)):
            curr.append(s2[i])
            del curr[0]
            if Counter(curr) == s1:
                return True
            
        return False