l, r = map(int, input().split())
 
if l == r:
    print(0)
else:
    print(2 ** (len(bin(l ^ r)[2:])) - 1)