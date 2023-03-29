class Solution:
    def findComplement(self, num: int) -> int:
        binary = list(bin(num).replace('0b', ''))

        for i in range(len(binary)):
            binary[i] = '0' if binary[i] == '1' else '1'

        return int(''.join(binary), 2)