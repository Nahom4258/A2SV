class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        c = list(c.items())
        c.sort(key=lambda x: x[1], reverse=True)

        return [x[0] for x in c][:k]