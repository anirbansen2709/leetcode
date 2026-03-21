# Given an integer array nums, find a subarray that has the largest product, and return the product. The test cases are generated so that the answer will fit in a 32-bit integer.
# Note that the product of an array with a single element is the value of that element.

# Logic
# prefix: Calculates the running product from left to right. suffix: Calculates the running product from right to left.
# Step-by-Step Breakdown:
# Initialization: * prefix and suffix are set to 1 (the multiplicative identity).
# max_prod is set to -infinity to ensure any valid product found in the array will overwrite it.
# The Loop: The loop runs n times (the length of the array).
# Zero Reset Check: It checks if either prefix or suffix became 0 in the previous step. If so, it resets them to 1. This effectively 
# "restarts" the subarray product calculation, ignoring the zero.
# Accumulation: * prefix is multiplied by the current element from the left (nums[idx]).
# suffix is multiplied by the corresponding element from the right (nums[len(nums) - idx - 1]).
# Update Max: It updates max_prod to be the highest value out of the current max_prod, the newly calculated prefix, 
# and the newly calculated suffix.
# Return: After checking all elements from both directions, max_prod holds the largest possible product.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = 1
        suffix = 1
        max_prod = float('-inf')
        prod = 1
        for idx in range(len(nums)):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
            prefix = prefix * nums[idx]
            suffix = suffix * nums[len(nums) - idx - 1]
            max_prod = max(max_prod, prefix, suffix)
        return max_prod

# TC - O(n)
# SC - O(1)
