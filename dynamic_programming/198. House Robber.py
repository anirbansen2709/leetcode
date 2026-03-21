# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that
# adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Recursion Solution
# starts evaluating from the last house in the array (length - 1) and works its way backward to the first house (0).
# The Setup: Inside rob, you find the length of the array and immediately call get_max_amount starting at the very last index.
# Base Cases: * if idx < 0: If you go out of bounds (which happens when you try to step back 2 houses from index 0 or 1), you return 0
# because there are no houses there.
# if idx == 0: If you reach the very first house, the maximum money you can get is just the money in that house (nums[0]).
# The Choices: For the current house at idx, you calculate two possibilities: rob: You take the money at nums[idx], and add it to the
# result of a recursive call that skips the adjacent house and goes to idx - 2.
# skip: You don't take the money at nums[idx], and instead just take whatever the maximum amount was up to the previous house at idx - 1.
# The Result: You return max(rob, skip), passing the best outcome back up the chain.

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

# Memoization
# create a dp array filled with -1 with size length
# if dp[idx] != -1: return dp[idx]. This is the core logic: if you've already calculated the max money for this specific idx before, 
# immediately return the saved answer instead of doing more recursion.
# Instead of just returning max(rob, skip), you first save it into your cache: dp[idx] = max(rob, skip) and then return dp[idx].

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
# SC - O(2n)

# Tabular Approach
# Instead of starting at the end and recursing backwards, you start at the beginning and loop forwards.
# The Setup: You create a dp array of size length filled with 0s.
# Base Case: You manually set the first house's value: dp[0] = nums[0].
# The Loop: You use a for loop starting from index 1 up to the end of the array.
# The Choices (Iterative):
# rob: You start with the current house's money (nums[idx]). Then, you have an if idx > 1: check. This ensures you don't go out of 
# bounds when looking 2 houses back. If it's safe, you add dp[idx - 2] (the max money from two houses ago) to rob.
# skip: You just look at the max money accumulated up to the previous house, which is already saved in dp[idx - 1].
# The Result: You store the maximum of those two choices into dp[idx]. When the loop finishes, the last element in your dp array 
# (dp[length - 1]) holds the final answer.

class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [0] * length
        dp[0] = nums[0]
        for idx in range(1, length):
            rob = nums[idx] 
            if idx > 1:
                rob += dp[idx - 2]
            skip = dp[idx - 1]
            dp[idx] = max(rob, skip)
        return dp[length - 1]
# TC - O(n)
# SC - O(n)
