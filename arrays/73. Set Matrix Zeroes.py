class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        c0 = 1
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    if col == 0:
                        c0 = 0
                    else:
                        matrix[0][col] = 0

        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        
        if matrix[0][0] == 0:
            for col in range(cols):
                matrix[0][col] = 0
        if c0 == 0:
            for row in range(rows):
                matrix[row][0] = 0

# TC - O(n * m)
# SC - O(1)
