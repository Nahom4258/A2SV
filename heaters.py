class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        n = len(heaters)

        def binary(house):
            left, right = 0, n-1

            while left <= right:
                mid = (left+right)//2
                if heaters[mid] < house:
                    left = mid+1
                elif heaters[mid] > house:
                    right = mid-1
                else:
                    left = mid
                    break

            l_c, r_c = inf, inf
            if left < 0 or left >= n:
                l_c = inf
            else:
                l_c = abs(heaters[left]-house)
                
            if right >= n or right < 0:
                r_c = inf
            else:
                r_c = abs(heaters[right]-house)

            return min(l_c, r_c)

        ans = 0
        for h in houses:
            ans = max(ans, binary(h))

        return ans