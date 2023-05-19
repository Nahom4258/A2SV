primes = [2, 3, 5, 7, 11, 13]
 
def prime_fact_no(n):
    ans = []
    
    while n not in primes:
        for prime in primes:
            if n % prime == 0:
                ans.append(prime)
                n /= prime
                break
            
    ans.append(int(n))
    
    return ans.count(2)
    
t = int(input())
 
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    count = 0
    
    for i in range(n):
        if arr[i] % 2 == 0:
            c = prime_fact_no(arr[i])
            count += c
            arr[i] = arr[i] // (2 ** c)
            
    arr.sort()
    
    arr[-1] *= (2**count)
    
    print(sum(arr))