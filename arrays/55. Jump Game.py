class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        goal = length - 1
        for idx in range(length - 2, -1, -1):
            if nums[idx] + idx >= goal:
                goal = idx
        return True if goal == 0 else False

# TC - O(n)
# SC - O(1)
