class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        min_index = len(nums)
        max_index = -1

        return [self.binarySearchLeft(nums, target), self.binarySearchRight(nums, target)]

    def binarySearchLeft(self, nums, target):
        start = 0
        end = len(nums) - 1
        index = len(nums)

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                index = min(index, mid)
                end = mid - 1

        return index if index < len(nums) else -1

    def binarySearchRight(self, nums, target):
        start = 0
        end = len(nums) - 1
        index = -1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                index = max(index, mid)
                start = mid + 1

        return index if index < len(nums) else -1