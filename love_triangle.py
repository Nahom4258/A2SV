vertices = int(input())
temp = list(map(int, input().split()))
 
for i in range(len(temp)):
    if i+1 ==  temp[temp[temp[i]-1]-1] and temp[i] != temp[temp[i]-1] != temp[temp[temp[i]-1]-1]:
        print('YES')
        exit()
print('NO')
