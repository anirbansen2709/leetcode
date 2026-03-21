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
        if len(nums) == 1:
            return nums[0]
        skip_first = self.get_max(0, nums[1:])
        skip_last = self.get_max(0, nums[:-1])
        return max(skip_first, skip_last)

#Memoization
class Solution:
    def get_max(self, idx, nums, dp):
        if idx >= len(nums):
            return 0
        if dp[idx] != -1:
            return dp[idx]
        rob = nums[idx] + self.get_max(idx+2, nums, dp)
        skip = self.get_max(idx+1, nums, dp)
        dp[idx] = max(rob, skip)
        return dp[idx]
        
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [-1 for _ in range(len(nums))]
        skip_first = self.get_max(0, nums[1:], list(dp))
        skip_last = self.get_max(0, nums[:-1], list(dp))
        return max(skip_first, skip_last)


# TC - O(n)
# SC - O(n)
