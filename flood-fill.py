class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        rowSize = len(image)
        colSize = len(image[0])
        visited = set()

        def helper(row, col):
            if row >= rowSize or col >= colSize or row < 0 or col < 0 or original != image[row][col] or image[row][col] == color:
                return

            image[row][col] = color

            helper(row-1, col)
            helper(row+1, col)
            helper(row, col-1)
            helper(row, col+1)

            return

        helper(sr, sc)

        return image