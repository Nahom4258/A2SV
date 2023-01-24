a = input()
 
n = list(map(int, input().split()))
m = list(map(int, input().split()))
 
ans = []
 
top_ptr = 0
bottom_ptr = 0
 
while bottom_ptr < len(m):
    if top_ptr >= len(n):
        top_ptr = len(n) - 1
        
    if n[top_ptr] < m[bottom_ptr] and top_ptr < len(n) - 1:
        top_ptr += 1
    elif n[top_ptr] < m[bottom_ptr] and top_ptr >= len(n) - 1:
        print(top_ptr + 1, end=' ')
        bottom_ptr += 1
    else:
        print(top_ptr, end=' ')
        bottom_ptr += 1
