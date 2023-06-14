class Solution:
    def numDecodings(self, s: str) -> int:
        memo = dict()

        def dp(index):
            if index >= len(s):
                return 1

            if s[index] == '0':
                return 0

            if index not in memo:
                single = dp(index+1)
                word = 0
                if index < len(s)-1 and int(s[index] + s[index+1])<=26:
                    word = dp(index+2)

                memo[index] = single + word

            return memo[index]
        
        return dp(0)