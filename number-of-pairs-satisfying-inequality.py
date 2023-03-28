class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        ans = 0

        # if len(nums) == 1:
        #     return 0
        
        def helper(arr):
            if len(arr) < 2:
                return arr

            # divide the array
            left, right = self.split(arr[::])

            left_merge = helper(left)
            right_merge = helper(right)

            i = len(left_merge) - 1
            j =  len(right_merge) - 1

            temp = 0
            while i >= 0 and j >= 0:
                if left_merge[i] <= right_merge[j] + diff:
                    temp += i + 1
                    j -= 1
                else:
                    i -= 1

            nonlocal ans
            ans += temp

            return self.merge(left_merge, right_merge)

        helper([nums1[i]-nums2[i] for i in range(len(nums1))])

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
                if left_arr[left_ptr] <= right_arr[right_ptr]:
                    ans.append(left_arr[left_ptr])
                    left_ptr += 1
                elif left_arr[left_ptr] > right_arr[right_ptr]:
                    ans.append(right_arr[right_ptr])
                    right_ptr += 1

            elif left_ptr < len(left_arr):
                ans.append(left_arr[left_ptr])
                left_ptr += 1

            elif right_ptr < len(right_arr):
                ans.append(right_arr[right_ptr])
                right_ptr += 1

        return ans