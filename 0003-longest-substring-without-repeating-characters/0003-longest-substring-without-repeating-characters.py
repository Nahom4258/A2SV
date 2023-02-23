class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []
        visited = set()
        max_length = 0
        
        left_ptr = 0
        right_ptr = 0
        
        while right_ptr < len(s) or left_ptr < len(s):
            if right_ptr >= len(s):
                right_ptr = len(s) - 1
            if s[right_ptr] not in visited:
                window.append(s[right_ptr])
                visited.add(s[right_ptr])
                max_length = max(max_length, len(window))
                right_ptr += 1
            else:
                visited.remove(s[left_ptr])
                del window[0]
                left_ptr += 1
            
        return max_length