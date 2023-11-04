class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        if x2-x1 != 0:
            slope = (y2-y1) / (x2-x1)
        else:
            slope = '#'

        for i in range(2, len(coordinates)):
            prev_x, prev_y = coordinates[i-1]
            x, y = coordinates[i]
            if x-prev_x != 0:
                temp_slope = (y-prev_y) / (x-prev_x)
            else:
                temp_slope = '#'

            if temp_slope != slope:
                return False

        return True