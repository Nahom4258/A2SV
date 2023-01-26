temp = list(map(int, input().split()))
 
n = temp[0]
k = temp[1]
 
arr = list(map(int, input().split()))
arr.sort()
 
if (k == 0 and arr[0] == 1) or (0 < k < n and arr[k-1] == arr[k]):
    print('-1')
elif k == 0 and arr[0] != 1:
    print(arr[0] - 1)
else:
    print(arr[k-1])
