class Solution:
    def get_max_amount(self, idx, nums, dp):
        if idx >= len(nums):
            return 0
        if dp[idx] != float('inf'):
            return dp[idx]
        dp[idx] = max(nums[idx] + self.get_max_amount(idx + 2, nums, dp), self.get_max_amount(idx + 1, nums, dp))
        return dp[idx]

    def rob(self, nums: List[int]) -> int:
        dp = [float('inf') for _ in range(len(nums))]
        return max(self.get_max_amount(0, nums[1:], dp), self.get_max_amount(0, nums[:-1], dp))


# TC - O(n)
# SC - O(n)
