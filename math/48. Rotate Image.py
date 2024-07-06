class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 1 2 3     1 4 7   7 4 1
        # 4 5 6     2 5 8   8 5 2
        # 7 8 9     3 6 9   9 6 3
        #transpose
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows - 1):
            for col in range(row + 1, cols):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        #reverse each row
        for row in range(rows):
            for col in range(cols//2):
                matrix[row][col], matrix[row][cols - col - 1] = matrix[row][cols - col - 1], matrix[row][col]

# TC - O(n * m)
# SC - O(1)
