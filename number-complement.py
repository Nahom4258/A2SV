class Solution:
    def findComplement(self, num: int) -> int:
        return num ^ int('1'*num.bit_length(), 2)