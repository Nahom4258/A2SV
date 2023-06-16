class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        left_min = []
        right_max = []

        for i in range(len(nums)):
            if not left_min:
                left_min.append(nums[i])
                continue

            left_min.append(min(left_min[-1], nums[i]))

        for i in range(len(nums)-1, -1, -1):
            if not right_max:
                right_max.append(nums[i])
                continue

            right_max.append(max(right_max[-1], nums[i]))

        right_max = right_max[::-1]

        for i in range(len(nums)):
            if left_min[i] < nums[i] and nums[i] < right_max[i]:
                return True

        return False