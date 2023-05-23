class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        ans = []
        for key in counter:
            ans.append((int(key), counter[key]))

        ans.sort(key=lambda x: x[1], reverse=True)

        return [ans[i][0] for i in range(k)]