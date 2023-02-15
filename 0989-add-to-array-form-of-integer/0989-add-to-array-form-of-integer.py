class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in range(len(num)):
            num[i] = str(num[i])
            
        return list(map(int, str(int(''.join(num)) + k)))