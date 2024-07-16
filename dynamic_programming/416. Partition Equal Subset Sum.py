class Solution:
    def can_get_total(self, subtotal, nums, idx, dp):
        if subtotal == 0:
            return True
        if idx == len(nums):
            return False
        if dp[idx][subtotal] != -1:
            return dp[idx][subtotal]
        dont = self.can_get_total(subtotal, nums, idx + 1, dp)
        take = False
        if nums[idx] >= subtotal:
            take = self.can_get_total(subtotal - nums[idx], nums, idx + 1, dp)
        dp[idx][subtotal] = dont or take
        return dp[idx][subtotal]

    def canPartition(self, nums: List[int]) -> bool:
        self.length = len(nums)
        total = sum(nums)
        if total % 2 == 1:
            return False
        subtotal = total // 2
        dp = [[-1 for _ in range(subtotal + 1)] for _ in range(self.length + 1)]
        return self.can_get_total(subtotal, nums, 0, dp)
