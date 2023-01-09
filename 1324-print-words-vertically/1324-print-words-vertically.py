class Solution:
    def printVertically(self, s: str) -> List[str]:
        answer = []
        s = s.split(' ')
        max_length = -1
        
        for word in s:
            max_length = max(len(word), max_length)
            
        for index, word in enumerate(s):
            if len(word) < max_length:
                s[index] = word + ' ' * (max_length - len(word))
                
        for index in range(max_length):
            ans = ''
            for j in range(len(s)):
                ans += s[j][index]
            answer.append(ans.rstrip())
            
        return answer
            
        