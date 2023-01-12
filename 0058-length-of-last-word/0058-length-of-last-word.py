class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ind = 0
        s = s.strip()
        
        for index in range(len(s) - 1, -1, -1):
            if s[index] == ' ':
                ind = index + 1
                break
                
        return len(s[ind:])