class Solution:
    def soupServings(self, n: int) -> float:
        if n > 5000:
            return 1.0

        memo = dict()

        #       a       b
        # 1.   100      0
        # 2.    75     25
        # 3.    50     50
        # 4.    25     75 

        def dp(a, b):
            if a == 0 and b == 0:
                return 0.5
            if a == 0:
                return 1
            if b == 0:
                return 0

            key = (a, b)
            if key in memo:
                return memo[key]

            op_1 = dp(max(0, a-100), b)
            op_2 = dp(max(0, a-75), max(0, b-25))
            op_3 = dp(max(0, a-50), max(0, b-50))
            op_4 = dp(max(0, a-25), max(0, b-75))

            memo[key] = 0.25 * (op_1 + op_2 + op_3 + op_4)

            return memo[key]

        a = dp(n, n)
        
        return a