class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:        
        ret = set()
        
        for num in nums1:
            if num in nums2:
                ret.add(num)
                
        return list(ret)