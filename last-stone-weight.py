class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            heapq._heapify_max(stones)
            a = heapq._heappop_max(stones)
            heapq._heapify_max(stones)
            b = heapq._heappop_max(stones)

            if a != b:
                stones.append(abs(a-b))

        return stones[0] if stones else 0