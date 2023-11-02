class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left_pointer = m - 1
        right_pointer = n - 1
        zero_pointer = m + n - 1
        
        while right_pointer >= 0:
            if left_pointer >= 0:
                if nums1[left_pointer] > nums2[right_pointer]:
                    nums1[zero_pointer] = nums1[left_pointer]
                    left_pointer -= 1
                else:
                    nums1[zero_pointer] = nums2[right_pointer]
                    right_pointer -= 1
                zero_pointer -= 1
            else:
                nums1[right_pointer] = nums2[right_pointer]
                right_pointer -=1