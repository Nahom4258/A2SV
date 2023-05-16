class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def primes(n):
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False

            p = 2
            while p * p <= n:
                if is_prime[p]:
                    for i in range(p * p, n + 1, p):
                        is_prime[i] = False
                p += 1

            primes = [i for i in range(n + 1) if is_prime[i]]
            return primes

        primes = primes(max(left, right))
        primes = list(filter(lambda x: left<=x<=right, primes))
        
        ans = [-1, -1]
        for i in range(1, len(primes)):
            if ans == [-1, -1]:
                ans = [primes[i-1], primes[i]]
            else:
                if primes[i] - primes[i-1] < ans[1] - ans[0]:
                    ans = [primes[i-1], primes[i]]

        return ans