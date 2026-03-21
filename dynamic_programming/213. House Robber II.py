# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. 
# That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses 
# were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Recursive
class Solution:
    def get_max(self, idx, nums):
        if idx >= len(nums):
            return 0
        rob = nums[idx] + self.get_max(idx+2, nums)
        skip = self.get_max(idx+1, nums)
        return max(rob, skip)
    def rob(self, nums: List[int]) -> int:
        skip_first = self.get_max(0, nums[1:])
        skip_last = self.get_max(0, nums[:-1])
        return max(skip_first, skip_last)

#Memoization
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
