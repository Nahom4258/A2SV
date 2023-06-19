class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)

        return max(counter, key=lambda x: counter[x])