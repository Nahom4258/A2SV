class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix = [0] * 1001
        passengers = 0

        for trip in trips:
            prefix[trip[1]] += trip[0]
            prefix[trip[2]] -= trip[0]

        for i in range(1001):
            passengers += prefix[i]
            if passengers > capacity:
                return False

        return True