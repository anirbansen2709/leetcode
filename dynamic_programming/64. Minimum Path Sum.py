class Solution:

    def get_min_sum(self, row, col):
        if row >= self.rows or col >= self.cols:
            return float('inf')
        if row == self.rows - 1 and col == self.cols - 1:
            return self.grid[row][col]
        down = self.get_min_sum(row, col + 1)
        right = self.get_min_sum(row + 1, col)
        return self.grid[row][col] + min(down, right)
        

    def minPathSum(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        return self.get_min_sum(0, 0)

# TC - O(Exponential)
# SC - O(n*m)

class Solution:

    def get_min_sum(self, row, col, min_sums):
        if row >= self.rows or col >= self.cols:
            return float('inf')
        if row == self.rows - 1 and col == self.cols - 1:
            return self.grid[row][col]
        if min_sums[row][col] != float(inf):
            return min_sums[row][col]
        down = self.get_min_sum(row, col + 1, min_sums)
        right = self.get_min_sum(row + 1, col, min_sums)
        min_sums[row][col] = self.grid[row][col] + min(down, right)
        return min_sums[row][col]
        

    def minPathSum(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        min_sums = [[float(inf) for _ in range(self.cols)] for _ in range(self.rows)]
        return self.get_min_sum(0, 0, min_sums)
# TC - O(n * m)
# SC - O(n * m)
