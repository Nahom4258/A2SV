n, m, k = map(int, input().split())
 
armies = []
ans = 0
 
for _ in range(m+1):
    armies.append(int(input()))
    
# print(armies)
for player in range(m):
    if bin(armies[player] ^ armies[-1]).count('1') <= k:
        ans += 1
        
print(ans)