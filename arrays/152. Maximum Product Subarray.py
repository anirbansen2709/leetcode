class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = 1
        suffix = 1
        max_prod = float('-inf')
        prod = 1
        for idx in range(len(nums)):
            if prefix == 0:
                prefix = 1
            elif suffix == 0:
                suffix = 1
            prefix = prefix * nums[idx]
            suffix = suffix * nums[len(nums) - idx - 1]
            max_prod = max(max_prod, prefix, suffix)
        return max_prod

# TC - O(n)
# SC - O(1)
