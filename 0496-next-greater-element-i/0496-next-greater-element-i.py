class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        result = []

        for item in nums2:
            while result and item > result[-1]:
                mapping[result.pop()] = item
            result.append(item)

        while result:
            mapping[result.pop()] = -1

        for item in nums1:
            result.append(mapping[item])

        return result