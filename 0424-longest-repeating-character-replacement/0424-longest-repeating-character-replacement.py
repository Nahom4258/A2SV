class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        ans = 0
        left = 0
        
        for right in range(len(s)):
            counter[s[right]] += 1
            while (right - left + 1) - max(counter.values()) > k:
                counter[s[left]] -= 1
                left += 1
                
            ans = max(ans, right - left + 1)

        return ans