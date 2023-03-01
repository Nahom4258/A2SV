class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def predict(start, end, p1_turn):
            if start == end:
                return [nums[start], 0] if p1_turn else [0, nums[start]]

            if p1_turn:
                ans1 = predict(start + 1, end, not p1_turn)
                ans1[0] += nums[start]
                ans2 = predict(start, end - 1, not p1_turn)
                ans2[0] += nums[end]

                return ans1 if ans1[0] >= ans2[0] else ans2

            else:
                ans1 = predict(start + 1, end, not p1_turn)
                ans1[1] += nums[start]
                ans2 = predict(start, end - 1, not p1_turn)
                ans2[1] += nums[end]

                return ans1 if ans1[1] >= ans2[1] else ans2

        ans = predict(0, len(nums) - 1, True)

        return True if ans[0] >= ans[1] else False