class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        _dict = dict()
        inside = set()
        mono = []
        
        for i in range(len(s)):
            _dict[s[i]] = i
            
        for i in range(len(s)):
            if s[i] in inside:
                continue
            
            while mono and mono[-1] > s[i] and _dict[mono[-1]] > i:
                inside.remove(mono[-1])
                mono.pop()
            mono.append(s[i])
            inside.add(s[i])
                
        return ''.join(mono)