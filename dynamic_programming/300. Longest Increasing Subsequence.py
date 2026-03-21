# Given an integer array nums, return the length of the longest strictly increasing subsequence. A subsequence is an array that can be derived from another array by deleting some or no elements
# without changing the order of the remaining elements.

# Top-Down Dynamic Programming / Memoization
# State Definition: The recursive function get_LIS(idx, prev, dp) determines the longest increasing subsequence starting from the current
# index (idx), given the index of the previously included element (prev).
# Base Case: If idx reaches the end of the array (len(self.nums)), there are no more elements to consider, so it returns 0.
# Memoization Check: Before computing, it checks if the result for the current idx and prev is already calculated and stored in the dp 
# table (if dp[idx][prev] != -1). If so, it returns the cached value to save time.
# Recursive Choices:
# Don't Take: You can always choose to skip the current element. The function calls itself with idx + 1 while keeping the same prev index.
# Take: You can only include the current element (self.nums[idx]) if no previous element was chosen (prev == -1) OR if the current element
# is strictly greater than the previously chosen element (self.nums[idx] > self.nums[prev]). If valid, you add 1 to the length and update
# the previous index to idx.
# Store and Return: It takes the maximum length between the "take" and "don't take" options, stores it in dp[idx][prev], and returns it.

class Solution:
    def get_LIS(self, idx, prev, dp):
        if idx == len(self.nums):
            return 0
        if dp[idx][prev] != -1:
            return dp[idx][prev]
        #dont
        dont = self.get_LIS(idx + 1, prev, dp)
        take = 0
        if prev == -1 or self.nums[idx] > self.nums[prev] :
            take = 1 + self.get_LIS(idx + 1, idx, dp)
        dp[idx][prev] = max(take, dont)
        return dp[idx][prev]

    def lengthOfLIS(self, nums: List[int]) -> int:
        self.nums = nums
        dp = [[-1 for _ in range(len(nums) + 1)] for _ in range(len(nums) + 1)]
        return self.get_LIS(0, -1, dp)

# TC - O(n^2)
# SC - O(n^2)
