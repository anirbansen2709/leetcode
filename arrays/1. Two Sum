class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()
        for idx, num in enumerate(nums):
            remaining = target - num
            if remaining in nums_dict:
                return [idx, nums_dict[remaining]]
            else:
                nums_dict[num] = idx

# TC - O(n)
# SC - O(n)
