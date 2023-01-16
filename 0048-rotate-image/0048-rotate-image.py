class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ans = []

        for row in range(len(matrix)):
            temp = []
            for col in range(len(matrix[0])):
                temp.append(matrix[col][row])

            ans.append(temp[::-1])
            
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = ans[i][j]