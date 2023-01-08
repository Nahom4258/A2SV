class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # variables
        ans = []
        start = 0
        
        # iterate through the space indices
        for space in spaces:
            ans.append(s[start:space])
            start = space
            
        # append the remaining
        ans.append(s[start:])  
        
        return ' '.join(ans)