class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Use binary search
        # Sort the list
        # For each search iteration, we reduce the list by half, discarding the other half as not containing the target value

        nums.sort()

        l, r = 0, len(nums)-1

        while l <= r:
            ind = (r+l)//2

            if nums[ind] < target:
                l = ind+1
            elif nums[ind] > target:
                r = ind-1
            else:
                return ind

        return -1