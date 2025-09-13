# Brute Force
# Try all possible combinations - TC - O(n ^ 4)

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        length = len(nums)
        answer = []
        nums.sort()
        for first in range(length - 3):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            for second in range(first + 1, length - 2):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                third = second + 1
                fourth = length - 1
                while third < fourth:
                    if (nums[first] + nums[second] + nums[third] + nums[fourth] == target):
                        answer.append([nums[first], nums[second], nums[third], nums[fourth]])
                        third += 1
                        fourth -= 1
                        while third < fourth and nums[third] == nums[third - 1]:
                            third += 1
                        while third < fourth and nums[fourth] == nums[fourth + 1]:
                            fourth -= 1
                    elif nums[first] + nums[second] + nums[third] + nums[fourth] > target:
                        fourth -= 1
                    else:
                        third += 1
        return answer

# TC - O(n ** 3)
# SC - O(1)
