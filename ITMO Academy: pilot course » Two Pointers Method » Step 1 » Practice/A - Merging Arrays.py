a = input()
 
n = list(map(int, input().split()))
m = list(map(int, input().split()))
 
ans = [0] * (len(n) + len(m))
 
top_ptr = 0
bottom_ptr = 0
current = 0
 
while top_ptr < len(n) or bottom_ptr < len(m):
    if top_ptr >= len(n):
        ans[current] = m[bottom_ptr]
        current += 1
        bottom_ptr += 1
        continue
    if bottom_ptr >= len(m):
        ans[current] = n[top_ptr]
        current += 1
        top_ptr += 1
        continue
        
    if n[top_ptr] > m[bottom_ptr]:
        ans[current] = m[bottom_ptr]
        bottom_ptr += 1
        current += 1
    elif n[top_ptr] < m[bottom_ptr]:
        ans[current] = n[top_ptr]
        top_ptr += 1
        current += 1
    else:
        ans[current] = n[top_ptr]
        current += 1
        top_ptr += 1
        ans[current] = m[bottom_ptr]
        bottom_ptr += 1
        current += 1
        
ans = [str(x) for x in ans]
print(' '.join(ans))
