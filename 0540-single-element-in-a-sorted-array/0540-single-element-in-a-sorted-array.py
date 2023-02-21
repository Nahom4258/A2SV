class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        counter = dict(Counter(nums))
        
        for key in counter:
            if counter[key] == 1:
                return int(key)