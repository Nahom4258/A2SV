class Solution:
    def countGoodNumbers(self, n: int) -> int:

        def mod(x, n, m):
            if n == 0:
                return 1
            if n == 1:
                return x

            if n % 2 == 0:
                return mod((x*x) % m, n//2, m)
            else:
                return x * mod((x*x) % m, (n-1)//2, m)


        MOD = 10**9 + 7

        odd_no = n//2
        even_no = odd_no + n%2

        evens = mod(5, even_no, MOD)
        primes = mod(4, odd_no, MOD)

        return (evens * primes) % MOD