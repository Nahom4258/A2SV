class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        new_num = []
        for val in nums:
            if val % 2 == 1:
                new_num.append(1)
            else:
                new_num.append(0)

        prefix_sum = 0
        counter = 0
        _dict = defaultdict(int)
        _dict[0] = 1

        for val in new_num:
            prefix_sum += val
            counter += _dict[prefix_sum - k]
            _dict[prefix_sum] += 1
                
        return counter