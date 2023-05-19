t = int(input())
 
for _ in range(t):
    n = int(input())
    
    arr = list(map(int, input().split(' ')))
    
    if n == 0:
        print(0)
    
    else:
        maxim = arr[0]
 
        for i in range(1, n):
            maxim &= arr[i]
                
        print(maxim)