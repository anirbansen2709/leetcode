# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
# The robot can only move either down or right at any point in time. Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the 
# bottom-right corner. The test cases are generated so that the answer will be less than or equal to 2 * 109.

# Top-Down Dynamic Programming (Memoization)
# 1. Initialization (uniquePaths method): It saves the grid dimensions (self.rows and self.cols).
# It creates a 2D list called dp initialized with -1. This acts as our memory (cache). -1 means "we haven't calculated the paths from
# this cell yet." It starts the recursive search by calling get_count(0, 0, dp).
# 2. The Recursive Engine (get_count method): This function calculates the number of paths from the current (row, col) to the
# destination. Base Case 1 (Out of Bounds): If the robot steps outside the grid (row >= self.rows or col >= self.cols), it returns 0
# because this is an invalid path. Base Case 2 (Destination Reached): If the robot reaches the exact bottom-right corner, it returns 1
# because it successfully found exactly one valid path to get there.
# Memoization Check: Before doing any heavy lifting, it checks if dp[row][col] != -1. If true, it immediately returns the saved result,
# skipping redundant calculations.
# Recursive Step: If it hasn't visited this cell before, it calculates the possible paths by simulating a step down (row + 1, col) and
# a step right (row, col + 1).
# Save and Return: It adds the results of the down and right paths together, saves the sum in dp[row][col], and returns it.

class Solution:
    def get_count(self, row, col, dp):
        if row >= self.rows or col >= self.cols:
            return 0
        if row == self.rows - 1 and col == self.cols - 1:
            return 1
        if dp[row][col] != -1:
            return dp[row][col]
        down = self.get_count(row + 1, col, dp)
        right = self.get_count(row, col + 1, dp)
        dp[row][col] = down + right
        return dp[row][col]
        
        
    def uniquePaths(self, m: int, n: int) -> int:
        self.rows = m
        self.cols = n
        dp = [[-1 for _ in range(self.cols)] for _ in range(self.rows)]
        return self.get_count(0, 0, dp)

# TC - O(n * m)
# SC - O(n * m)
