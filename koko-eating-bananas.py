class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        minim = end + 1

        while start <= end:
            mid = (start + end) // 2
            time = self.findTime(piles, mid)
            # print('idx: ', mid, 'time: ', time)
            if time <= h:
                minim = min(minim, mid)
                end = mid - 1
            elif time > h:
                start = mid + 1

        return minim


    def findTime(self, arr, eats):
        time_count = 0
        for val in arr:
            if val <= eats:
                time_count += 1
            else: 
                time_count += ceil(val/eats)

        return time_count