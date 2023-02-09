https://codeforces.com/problemset/problem/1174/B

n = int(input())
a = list(map(int, input().split()))
 
even = False
odd = False
 
for digit in a:
    if digit % 2 == 0:
        even = True
    elif digit % 2 == 1:
        odd = True
        
if even and odd:
    a.sort()
 
print(*a)
