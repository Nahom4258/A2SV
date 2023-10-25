class Solution:
    def countGoodNumbers(self, n: int) -> int:

        def mod(x, n, mod):
            result = 1
            x = x % mod
            while n > 0:
                if n % 2 == 1:
                    result = (result * x) % mod
                x = (x * x) % mod
                n = n // 2
            return result

        MOD = 10**9 + 7

        odd_no = n//2
        even_no = odd_no + (0 if n%2==0 else 1)

        evens = mod(5, even_no, MOD)
        primes = mod(4, odd_no, MOD)

        return (evens * primes) % MOD