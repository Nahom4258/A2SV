class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)

        for i in range(len(nums)):
            nums[i] = (i, nums[i])        

        def merge(left, right):
            l = 0
            r = 0

            ans = []

            while l < len(left) or r < len(right):
                if l < len(left) and r < len(right):
                    if left[l][1] <= right[r][1]:
                        ans.append(left[l])
                        l += 1
                    else:
                        ans.append(right[r])
                        r += 1
                elif l < len(left):
                    ans.append(left[l])
                    l += 1  
                elif r < len(right):
                    ans.append(right[r])
                    r += 1
            return ans

        def mergeSortWhileCount(arr, l, r):
            nonlocal ans

            if l == r:
                return [arr[l]]

            m = l + (r - l) // 2

            left = mergeSortWhileCount(arr, l, m)
            right = mergeSortWhileCount(arr, m + 1, r)

            lptr = len(left) - 1
            rptr = len(right) - 1

            while lptr >= 0 and rptr >= 0:
                if left[lptr][1] > right[rptr][1]:
                    ans[left[lptr][0]] += rptr + 1
                    lptr -= 1
                else:
                    rptr -= 1

            return merge(left, right)

        mergeSortWhileCount(nums, 0, len(nums) - 1)
        return ans