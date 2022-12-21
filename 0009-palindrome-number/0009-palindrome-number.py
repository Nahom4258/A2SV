class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans = True
        for i, digit in enumerate(str(x)):
            if digit != str(x)[len(str(x)) - i - 1]:
                ans = False
                
        return ans
            
        