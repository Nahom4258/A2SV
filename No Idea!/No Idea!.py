length = input().split()
elements = input().split()
A = set(input().split())
B = set(input().split())

happiness = 0
for element in elements:
    if element in A:
        happiness += 1
    if element in B:
        happiness -= 1
        
print(happiness)
