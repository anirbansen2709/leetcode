class Solution:
    def get_paths(self, row, col, dp):
        if row == 0 and col == 0:
            return 1
        if row < 0 or col < 0:
            return 0
        if dp[row][col] != float('inf'):
            return dp[row][col]
        dp[row][col] = self.get_paths(row - 1, col, dp) + self.get_paths(row, col - 1, dp)
        return dp[row][col]

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[float('inf') for _ in range(n+1)] for _ in range(m+1)]
        return self.get_paths(m - 1, n - 1, dp)

# TC - O(n * m)
# SC - O(n * m)
