import heapq
 
for _ in range(int(input())):
    n = int(input())
    arr = list(map(lambda x: -1* int(x), input().split()))
    ans = 0
    talks = []
    for i in range(n):
        arr[i] = (arr[i], i)
    
    heapq.heapify(arr)
    while len(arr) > 1:
        ele1, idx1 = heapq.heappop(arr)
        ele2, idx2 = heapq.heappop(arr)
        
        if ele1 < 0 and ele2 < 0:
            talks.append((idx2+1, idx1+1))
            ans+=1
            
        ele1 += 1
        ele2 += 1
        if ele1 < 0:
            heapq.heappush(arr, (ele1, idx1))
        if ele2 < 0:
            heapq.heappush(arr, (ele2, idx2))
 
    print(ans)
    for t in talks:
        print(*t)