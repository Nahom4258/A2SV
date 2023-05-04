class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            a = heappop(stones)
            b = heappop(stones)

            if a != b:
                stones.append(-abs(a-b))

        return -stones[0] if stones else 0