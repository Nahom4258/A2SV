class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_sum = [0] * (len(s) + 1)
        s = list(s)
        
        for shift in shifts:
            # forward
            if shift[2] == 1:
                prefix_sum[shift[0]] += 1
                prefix_sum[shift[1]+1] -= 1
            # backward
            else:
                prefix_sum[shift[0]] -= 1
                prefix_sum[shift[1]+1] += 1
                
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] += prefix_sum[i-1]
                    
        for i in range(len(prefix_sum) - 1):
            s[i] = chr(((ord(s[i]) + prefix_sum[i] - 97) % 26) + 97)
            
        return ''.join(s)