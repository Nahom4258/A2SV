class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        p = 0
        needle_n = len(needle)
        haystack_n = len(haystack)

        def hash(word):
            ans = 0
            n = len(word)
            for i in range(n):
                ans += (ord(word[i])-96) * 26**(n-i-1)

            return ans

        p = hash(needle)

        left = 0
        right = needle_n-1
        start = hash(''.join(haystack[:right+1]))
        
        if start == p:
            return 0
        while right < haystack_n-1:
            right += 1
            curr = ((start - ((ord(haystack[left])-96) * (26**(needle_n-1)))) * 26) + (ord(haystack[right])-96)
            left += 1
            if curr == p:
                return left
            start = curr
            
        return -1