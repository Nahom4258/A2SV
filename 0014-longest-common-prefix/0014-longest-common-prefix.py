class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = 201
        ans = ''
        for word in strs:
            smallest = min(len(word), smallest)
            
        for i in range(smallest):
            shared = True
            letter = strs[0][i]
            for word in strs:
                if word[i] != letter:
                    shared = False
            if shared:
                ans += letter
            else:
                break
                
        return ans
            
            