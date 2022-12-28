# Enter your code here. Read input from STDIN. Print output to STDOUT

# accept input
A = set(input().split())
n = int(input())
display = 'True'

for i in range(n):
    o = set(input().split())
    if len(A) <= len(o):
        display = 'False'
        break
    else:
        if not A.issuperset(o):
            display = 'False'
            break
        
print(display)
