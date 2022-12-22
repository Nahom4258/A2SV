class Solution:
    def freqAlphabets(self, s: str) -> str:
        lp = 0
        rp = 2
        ans = ''
                
        while lp <= len(s) - 1:
            if rp <= len(s) - 1 and s[rp] == '#':
                ans += chr(int(s[lp:rp]) + 96)
                lp += 3
                rp += 3
            else:
                ans += chr(int(s[lp]) + 96)
                lp += 1
                rp += 1
                
        return ans