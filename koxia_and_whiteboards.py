import heapq
 
t = int(input())
 
for _ in range(t):
    n, m = map(int, input().split(' '))
 
    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))
    
    
    heapq.heapify(a)
    
    i = 0
    while i < len(b):
        heapq.heappop(a)
        heapq.heappush(a, b[i])
        i += 1
        
    # print('ans; ', a)
        
    print(sum(a))