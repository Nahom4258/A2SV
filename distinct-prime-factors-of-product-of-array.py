class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        factors = set()

        def prime_factors(n):
            i = 2
            while i*i <= n:
                while n % i == 0:
                    n //= i
                    factors.add(i)
                if i == 2:
                    i += 1
                else:
                    i += 2
            if n > 1:
                factors.add(n)

        for val in nums:
            prime_factors(val)

        # print('prod: ', factors)

        return len(factors)