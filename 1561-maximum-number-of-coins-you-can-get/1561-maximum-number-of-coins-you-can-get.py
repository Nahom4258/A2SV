class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        left_ptr = 0
        right_ptr = len(piles) - 2
        maxim = 0
        
        piles.sort()
        
        while left_ptr < right_ptr:
            maxim += piles[right_ptr]
            right_ptr -= 2
            left_ptr += 1
            
        return maxim