class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        answer = []
        for first in range(length - 2):
            num_set = set()
            for second in range(first + 1, length - 1):
                left = - (nums[first] + nums[second])
                if left in num_set:
                    temp = [nums[first], nums[second], left]
                    temp.sort()
                    answer.append(tuple(temp))
                num_set.add(nums[second])
        return list(set(answer))

# TC - O(n ** 2)
# SC - O(n)
