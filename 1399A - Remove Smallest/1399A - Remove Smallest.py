t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = 'YES'
    
    a.sort()
    
    for i in range(n - 1):
        if abs(a[i] - a[i + 1]) > 1:
            ans = 'NO'
            break
        
    print(ans)
