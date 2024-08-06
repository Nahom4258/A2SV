class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0

        left_ptr = 0
        right_ptr = len(height)-1

        while left_ptr < right_ptr:
            curr_area = min(height[left_ptr], height[right_ptr]) * (right_ptr-left_ptr)
            ans = max(ans, curr_area)

            if height[left_ptr] < height[right_ptr]:
                left_ptr += 1
            elif height[right_ptr] < height[left_ptr]:
                right_ptr -= 1
            else:
                left_ptr += 1
                right_ptr -= 1

        return ans