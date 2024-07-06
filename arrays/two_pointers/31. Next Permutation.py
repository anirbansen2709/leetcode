class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        pivot = None
        for idx in range(length - 2, -1, -1):
            if nums[idx] < nums[idx + 1]:
                pivot = idx
                break
        if pivot is None:
            nums.reverse()
        else:
            for idx in range(length - 1, pivot, -1):
                if nums[pivot] < nums[idx]:
                    nums[pivot], nums[idx] = nums[idx], nums[pivot]
                    break

            nums[pivot + 1:] = nums[pivot + 1:][::-1]

# TC - O(n)
# SC - O(1)
