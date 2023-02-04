class Solution:
    def addDigits(self, num: int) -> int:
        num = list(str(num))
        
        while True:
            if len(num) == 1:
                return int(''.join(num))
            
            sum = 0
            for digit in num:
                sum += int(digit)
            
            num = list(str(sum))
            
        return 0