class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        happy = False
        
        n = list(str(n))
        
        while True:
            sum = 0
            for digit in n:
                sum += int(digit) * int(digit)
                
            if sum == 1:
                happy = True
                break
            if sum in visited:
                happy = False
                break
                
            visited.add(sum)
            n = list(str(sum))
                
        return happy