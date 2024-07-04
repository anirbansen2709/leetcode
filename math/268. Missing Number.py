class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actual = sum(nums)
        length = len(nums)
        expected = length * (length + 1) // 2
        return expected - actual

# TC - O(n)
# SC - O(1)
