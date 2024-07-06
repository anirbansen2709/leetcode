class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_seq = 0
        length = 0

        for num in nums:
            if num - 1 not in nums_set:
                length = 0
                while num + length in nums_set:
                    length += 1
                max_seq = max(max_seq, length)
                
        return max_seq

# TC - O(n)
# SC - O(n)
