class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        cur = float('-inf')
        for num in nums:
            cur = max(cur + num, num)
            max_sum = max(max_sum, cur)
        return max_sum

# TC - O(n)
# SC - O(1)
