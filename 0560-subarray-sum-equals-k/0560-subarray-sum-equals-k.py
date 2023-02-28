class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = count = 0
        dic = dict()
        for i in nums:
            prefix_sum += i
            if prefix_sum == k:
                count += 1
            if dic.get(prefix_sum - k):
                count += dic.get(prefix_sum - k)
            if dic.get(prefix_sum):
                dic[prefix_sum] += 1
            else:
                dic[prefix_sum] = 1
        return count