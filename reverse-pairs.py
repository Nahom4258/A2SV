class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = 0

        if len(nums) == 1:
            return 0
        
        def helper(arr):
            if len(arr) < 2:
                return arr

            # divide the array
            left, right = self.split(arr[::])

            left_merge = helper(left)
            right_merge = helper(right)

            i = 0
            j = 0

            temp = 0
            while i < len(left_merge) and j < len(right_merge):
                if left_merge[i] > 2 * right_merge[j]:
                    temp += len(left_merge) - i
                    j += 1
                else:
                    i += 1

            nonlocal ans
            ans += temp

            return self.merge(left_merge, right_merge)

        helper(nums)

        return ans

    def split(self, arr):
        mid = (0 + len(arr)) // 2

        return arr[:mid], arr[mid:]

    def merge(self, left_arr, right_arr):
        left_ptr = 0
        right_ptr = 0
        ans = []
        while left_ptr < len(left_arr) or right_ptr < len(right_arr):
            # both available
            if left_ptr < len(left_arr) and right_ptr < len(right_arr):
                # left is smaller
                if left_arr[left_ptr] < right_arr[right_ptr]:
                    ans.append(left_arr[left_ptr])
                    left_ptr += 1
                elif left_arr[left_ptr] > right_arr[right_ptr]:
                    ans.append(right_arr[right_ptr])
                    right_ptr += 1
                else:
                    ans.append(left_arr[left_ptr])
                    ans.append(left_arr[left_ptr])
                    left_ptr += 1
                    right_ptr += 1

            elif left_ptr < len(left_arr):
                ans.append(left_arr[left_ptr])
                left_ptr += 1

            elif right_ptr < len(right_arr):
                ans.append(right_arr[right_ptr])
                right_ptr += 1

        return ans