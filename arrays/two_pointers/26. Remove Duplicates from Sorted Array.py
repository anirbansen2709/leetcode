class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        length = len(nums)
        for right in range(1, length):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
            right +=1
        return left

# TC - O(n)
# SC - O(1)
