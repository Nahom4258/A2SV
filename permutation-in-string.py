class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1)-1
        target = Counter(s1)

        curr = Counter(s2[left:right+1])

        if curr == target:
            return True

        while right < len(s2)-1:
            if s2[left] in curr and curr[s2[left]] > 1:
                curr[s2[left]] -= 1
            elif s2[left] in curr and curr[s2[left]] == 1:
                del curr[s2[left]]

            left += 1
            right += 1

            if s2[right] in curr:
                curr[s2[right]] += 1
            else:
                curr[s2[right]] = 1

            if curr == target:
                return True

        return False