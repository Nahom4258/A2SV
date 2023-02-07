temp = list(map(int, input().split()))
n = temp[0]
m = temp[1]
 
table = []
for _ in range(n):
    table.append(list(input()))
    
rotated_table = []
for col in range(m):
    temp = []
    for row in range(n):
        temp.append(table[row][col])
        
    rotated_table.append(temp)
    
ans = ''
 
for row in range(n):
    for col in range(m):
        if table[row].count(table[row][col]) == 1 and rotated_table[col].count(table[row][col]) == 1:
            ans += table[row][col]
            
print(ans)
