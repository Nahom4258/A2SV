class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def helper(s, index):
            if index == n-1:
                return s

            return helper(s + '1' + self.reverse(self.invert(s)), index + 1)

        return helper('0', 0)[k-1]

    def invert(self, s):
        s = list(s)
        for i in range(len(s)):
            s[i] = '0' if s[i] == '1' else '1'

        return ''.join(s)

    def reverse(self, s):
        s = list(s)
        s.reverse()

        return ''.join(s)