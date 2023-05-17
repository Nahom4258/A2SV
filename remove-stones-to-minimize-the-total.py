class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-x for x in piles]

        heapq.heapify(piles)

        while k > 0:
            num = heapq.heappop(piles) * -1
            heapq.heappush(piles, (num-floor(num/2)) * -1)

            k -= 1

        # print("ans: ", piles)
        piles = [-x for x in piles]

        return sum(piles)