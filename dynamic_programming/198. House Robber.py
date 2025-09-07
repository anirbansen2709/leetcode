# Recursion Solution
class Solution:
    def get_max_amount(self, idx, nums):
        if idx < 0 :
            return 0
        if idx == 0:
            return nums[0]
        rob = nums[idx] + self.get_max_amount(idx - 2, nums)
        skip = self.get_max_amount(idx - 1, nums)
        return max(rob, skip)

    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        return self.get_max_amount(length - 1, nums)

# TC - O(2^n)
# SC - O(n)

class Solution:
    def get_max_amount(self, idx, nums, dp):
        if idx < 0 :
            return 0
        if idx == 0:
            return nums[0]
        if dp[idx] != -1:
            return dp[idx]
        rob = nums[idx] + self.get_max_amount(idx - 2, nums, dp)
        skip = self.get_max_amount(idx - 1, nums, dp)
        dp[idx] = max(rob, skip)
        return dp[idx]

    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [-1 for _ in range(length + 1)]
        return self.get_max_amount(length - 1, nums, dp)

# TC - O(n)
# SC - O(n)
