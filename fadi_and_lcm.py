from math import lcm
 
x = int(input())
n = x
factors = []
 
i = 1
while i*i <= x:
    if x % i == 0:
        factors.append(i)
        if x//i != i:
            factors.append(x//i)
    i += 1
    
factors.sort()
val = (1, x)
left = 0
right = len(factors) - 1
 
while left < right:
    right = len(factors) - 1 - left
    
    if lcm(factors[left], factors[right]) == n and max(factors[left], factors[right]) < max(val):
        val = (factors[left], factors[right])
        
    left += 1
    right -= 1
    
print(val[0], val[1])