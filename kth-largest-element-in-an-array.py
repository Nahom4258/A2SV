class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        temp = []

        for num in nums:
            heapq.heappush(temp, -num)

        ans = 0
        for i in range(k-1):
            heapq.heappop(temp)

        return -1 * heapq.heappop(temp)