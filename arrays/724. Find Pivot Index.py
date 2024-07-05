class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        pre = 0
        for idx, num in enumerate(nums):
            if pre == total - num - pre:
                return idx
            pre += num
        return -1

# TC - O(n)
# SC - O(1)
