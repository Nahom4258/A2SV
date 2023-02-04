class Solution:
    def reverseVowels(self, s: str) -> str:
        left_ptr = 0
        right_ptr = len(s) - 1
        s = list(s)
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        
        while left_ptr < right_ptr:
            if s[left_ptr] in vowels and s[right_ptr] in vowels:
                s[left_ptr], s[right_ptr] = s[right_ptr], s[left_ptr]
                left_ptr += 1
                right_ptr -= 1
                continue
            
            if s[left_ptr] not in vowels:
                left_ptr += 1
                continue
                
            if s[right_ptr] not in vowels:
                right_ptr -= 1
                continue
                
        return ''.join(s)