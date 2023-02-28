class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        postfix = [0] * n
        ans = [0] * n
        
        # calculate prefix product
        prefix[0] = 1
        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]
            
        # calculate postfix product
        postfix[-1] = 1
        for i in range(len(nums)-2, -1, -1):
            postfix[i] = nums[i+1] * postfix[i+1]
            
        for i in range(n):
            ans[i] = prefix[i] * postfix[i]
            
        return ans
            
        