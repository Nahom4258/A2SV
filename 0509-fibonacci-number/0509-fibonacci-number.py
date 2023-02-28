class Solution:
    def fib(self, n: int) -> int:
        add = 1
        left_ptr = 0
        right_ptr = 1
        ans = [0,1]
        
        if n == 0:
            return 0
        
        for i in range(n-1):
            ans.append(ans[left_ptr] + ans[right_ptr])
            left_ptr += 1
            right_ptr += 1
            
        return ans[-1]