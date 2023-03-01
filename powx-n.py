class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if n == 0:
        #     return 1

        # def pow(num, times):
        #     if times < 2:
        #         return num

        #     return pow(num * x, times - 1)

        # ans = pow(x, abs(n))

        # return ans if n >= 0 else 1/ans

        if n == 0:
            return 1
        
        pow = abs(n)

        res = 0

        if pow % 2 == 0:
            res = self.myPow(x * x, pow / 2)
        else:
            res = self.myPow(x * x, (pow - 1) /2) * x

        return res if n >= 0 else 1/res