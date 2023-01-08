def evenSum(nums):
    ans = 0
    
    for num in nums:
        if num % 2 == 0:
            ans += num
            
    return ans

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # variables
        answer = []
        even_sum_init = evenSum(nums)
        
        for query in queries:
            if nums[query[1]] % 2 == 0:
                even_sum_init -= nums[query[1]]
            nums[query[1]] = nums[query[1]] + query[0]
            if nums[query[1]] % 2 == 0:
                even_sum_init += nums[query[1]]
                answer.append(even_sum_init)
            else:
                answer.append(even_sum_init)
            
        return answer