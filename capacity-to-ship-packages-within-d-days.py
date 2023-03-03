class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start = 1
        end = sum(weights) - 1
        minim = end + 1

        while start <= end:
            mid = (start + end) // 2
            # print('idx: ' , mid)
            days_taken = self.getDays(weights, mid, days)
            # print('days taken: ', days_taken)
            print('--------------')
            if days_taken < days:
                minim = min(minim, mid)
                end = mid - 1
            elif days_taken >= days:
                start = mid + 1

        return minim

    def getDays(self, arr, takes, days):
        if max(arr) > takes:
            return days + 1

        days_taken = 0
        temp = takes

        for weight in arr:
            if temp >= weight:
                temp -= weight
            else:
                days_taken += 1
                temp = takes
                temp -= weight

        return days_taken