class Solution:
    def reverse(self, left, right):
        while left < right:
            self.nums[left], self.nums[right] = self.nums[right], self.nums[left]
            left += 1
            right -= 1
        return

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.nums = nums
        length = len(nums)
        self.reverse(0, length - k - 1)
        self.reverse(length - k, length - 1)
        self.reverse(0, length - 1)

# TC - O(n)
# SC - O(1)
