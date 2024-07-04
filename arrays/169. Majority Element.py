class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = None
        count = 0
        for num in nums:
            if count == 0:
                majority = num
            elif majority == num:
                count += 1
            else:
                count -= 1
        return majority

# TC - O(n)
# SC - O(1)
