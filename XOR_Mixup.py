t = int(input())
 
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    ans = 0
    found = False
    
    for i in range(n):
        temp = 0
        for j in range(n):
            if i != j:
                temp ^= nums[j]
                
        if temp == nums[i]:
            ans = nums[i]
            break
        
    print(ans)