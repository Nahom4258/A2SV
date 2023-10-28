class DetectSquares:

    def __init__(self):
        self.p_count = defaultdict(int)
        self.x_axis = defaultdict(set)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.p_count[(x, y)] += 1
        self.x_axis[x].add(y)

    def count(self, point: List[int]) -> int:
        curr_x, curr_y = point
        curr_count = 0
        ans = 0
        # check if there exists any point on horizontal axis of curr
        if self.x_axis[curr_x]:
            # iterate through all the horizontal axis points and find the other 2 points
            for horiz_y in self.x_axis[curr_x]:
                temp = 0
                if horiz_y != curr_y:
                    l = abs(curr_y - horiz_y)
                    horiz_x, horiz_y = curr_x, horiz_y
                    # left side
                    # check the left from the curr_point and left from the horiz point
                    if self.p_count[(curr_x-l, curr_y)] and self.p_count[(horiz_x-l, horiz_y)]:
                        left = (self.p_count[(curr_x-l, curr_y)] * self.p_count[(horiz_x-l, horiz_y)] * self.p_count[(horiz_x, horiz_y)] * (curr_count + 1))
                        temp += left

                    # right side
                    # check the right from the curr point and right from the horiz point
                    if self.p_count[(curr_x+l, curr_y)] and self.p_count[(horiz_x+l, horiz_y)]:
                        right = (self.p_count[(curr_x+l, curr_y)] * self.p_count[(horiz_x+l, horiz_y)] * self.p_count[(horiz_x, horiz_y)] * (curr_count + 1))
                        temp += right
                    
                ans += temp

        return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)