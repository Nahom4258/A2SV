class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = defaultdict(list)
        n = len(nums)

        for i in range(n):
            num = nums[i]
            if num not in indices:
                indices[num].append(i)
            else:
                if len(indices[num]) < 2 and i not in indices[num]:
                    indices[num].append(i)

        nums.sort()
        l, r = 0, n-1
        while l < r:
            add = nums[l] + nums[r]
            if add == target:
                if nums[l] == nums[r]:
                    return indices[nums[l]]

                return [indices[nums[l]][0], indices[nums[r]][0]]
            elif add < target: 
                l += 1
            else:
                r -= 1

        return []