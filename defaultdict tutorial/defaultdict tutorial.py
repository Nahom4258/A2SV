# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

# accept inputs
temp = input().split()
n = int(temp[0])
m = int(temp[1])
A = list()
B = list()

my_dict = defaultdict(list)

for i in range(n + m):
    if i in range(n):
        # A.append(input())
        my_dict[input()].append(i + 1)
    else:
        B.append(input())
        
for b in B:
    if b in my_dict:
        for val in my_dict[b]:
            print(val, end=' ')
    else:
        print(-1, end=' ')
    print()
