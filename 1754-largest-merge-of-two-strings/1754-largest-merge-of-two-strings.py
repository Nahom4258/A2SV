class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        _word1 = list(word1) 
        _word2 = list(word2)
        ans = ''

        while _word1 and _word2:
            if _word1 > _word2:
                ans += _word1.pop(0)
            else:
                ans += _word2.pop(0) 
                
        return ans + ''.join(_word1) + ''.join(_word2)