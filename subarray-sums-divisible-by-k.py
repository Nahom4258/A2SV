class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        counter = 0
        _dict = defaultdict(int)
        _dict[0] = 1

        for val in nums:
            prefix_sum += val
            counter += _dict[prefix_sum % k]
            _dict[prefix_sum % k] += 1
                
        return counter