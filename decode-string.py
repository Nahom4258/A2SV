class Solution:
    def decodeString(self, s: str) -> str:
        def helper(s, i):
            ans = ""
            num = 0
            while i < len(s):
                if s[i].isdigit():
                    num = num * 10 + int(s[i])
                elif s[i] == '[':
                    decodedStr, i = helper(s, i + 1)
                    ans += num * decodedStr
                    num = 0
                elif s[i] == ']':
                    return ans, i
                else:
                    ans += s[i]
                i += 1
            
            return ans

        return helper(s, 0)