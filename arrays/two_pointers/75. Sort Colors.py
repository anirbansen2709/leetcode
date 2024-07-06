class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        idx = 0
        while idx <= right:
            if nums[idx] == 0:
                nums[left], nums[idx] = nums[idx], nums[left]
                left += 1
            if nums[idx] == 2:
                nums[right], nums[idx] = nums[idx], nums[right]
                right -= 1
                idx -= 1
            idx += 1

#TC - O(n)
#SC - O(1)
