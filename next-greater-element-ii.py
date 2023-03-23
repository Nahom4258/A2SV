class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # counter = defaultdict(lambda:-1)
        result = [-1] * len(nums)
        monotonic = []

        for j in range(2):
            for i in range(len(nums)):

                while monotonic and nums[monotonic[-1]] < nums[i]:
                    result[monotonic.pop()] = nums[i]
                
                monotonic.append(i)

        return result