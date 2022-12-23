class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        distance = 20001
        smallest_index = 10001
        
        for index, point in enumerate(points):
            if point[0] == x or point[1] == y:
                if distance > (abs(x - point[0]) + abs(y - point[1])):
                    smallest_index = index
                    distance = abs(x - point[0]) + abs(y - point[1])
                    
        if smallest_index == 10001:
            smallest_index = -1
                    
        return smallest_index