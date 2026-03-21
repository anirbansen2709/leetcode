# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that
# adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Recursion Solution
# Direction: Starts evaluating from the first house in the array (index 0) and works its way forward to the end of the array.
# The Setup: Inside rob, you store the array and its length as class variables (self.nums and self.length), and then immediately call 
# get_max starting at the very first index (0).
# Base Cases: * if idx == self.length: If you go out of bounds (past the last house), you return 0 because there are no more houses 
# left to rob.
# if idx == self.length - 1: If you reach the very last house, the maximum money you can get from this point forward is just the money
# in that specific house (self.nums[idx]).
# The Choices: For the current house at idx, you calculate two possibilities:
# skip: You don't take the money at the current house, and instead see what the maximum amount is if you just move to the very next
# house at idx + 1.
# rob: You take the money at the current house (self.nums[idx]), and add it to the result of a recursive call that skips the adjacent 
# house and jumps ahead to idx + 2.
# The Result: You return max(skip, rob), passing the best outcome back up the chain.

class Solution:
    def get_max(self, idx):
        if idx == self.length:
            return 0
        if idx ==  self.length - 1:
            return self.nums[idx]
        skip = self.get_max(idx + 1)
        rob = self.nums[idx] + self.get_max(idx + 2)
        return max(skip, rob)

    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        self.length = len(self.nums)
        return self.get_max(0)

# TC - O(2^n)
# SC - O(n)

# Memoization
# The Setup: Create a dp array of size length, filled with -1s, to act as our cache.
# The Cache Check (Core Logic): Before doing any heavy recursion, check if dp[idx] != -1. 
# If it isn't -1, we've already calculated the max money for this specific index. 
# We immediately return the saved answer to prevent redundant recursive calls.
# Saving the State: Instead of just returning max(skip, rob) at the end, we first save the 
# calculated best outcome into our cache (dp[idx] = max(skip, rob)) and then return it.

class Solution:
    def get_max(self, idx, dp):
        if idx == self.length:
            return 0
        if idx ==  self.length - 1:
            return self.nums[idx]
        if dp[idx] != -1:
            return dp[idx]
        skip = self.get_max(idx + 1, dp)
        rob = self.nums[idx] + self.get_max(idx + 2, dp)
        dp[idx] = max(skip, rob)
        return dp[idx]

    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        self.length = len(self.nums)
        dp = [-1 for _ in range(self.length)]
        return self.get_max(0, dp)

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
