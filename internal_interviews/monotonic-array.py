class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc_stack = []
        n = len(nums)

        direction = 0   # 0 - unknown, 1 - increasing, 2 - decreasing

        for i in range(n-1):
            if direction == 0:
                if nums[i] < nums[i+1]:
                    direction = 1
                elif nums[i] > nums[i+1]:
                    direction = -1
            elif direction == 1 and nums[i] > nums[i+1]:
                return False
            elif direction == -1 and nums[i] < nums[i+1]:
                return False

        return True