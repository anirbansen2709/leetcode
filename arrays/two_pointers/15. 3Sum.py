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
# might run into a TLE

# Optimised Solution

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        nums.sort()
        first = 0
        result = []
        while first < length - 2:
            # no duplicate values for first
            while 0 < first < length - 1 and nums[first] == nums[first - 1]:
                first += 1
            second = first + 1
            third = length - 1
            while second < third :
                total = nums[first] + nums[second] + nums[third]
                # if triplet found
                if total == 0:
                    result.append([nums[first], nums[second], nums[third]])
                    second += 1
                    # no duplicate value for second
                    while second < third and nums[second] == nums[second - 1]:
                        second += 1
                    third -= 1
                    # no duplicate value for third
                    while third >= second and nums[third] == nums[third + 1]:
                        third -=1
                elif total > 0: # if sum greater
                    # reduce third without repitition
                    third -= 1
                    while third >= second and nums[third] == nums[third + 1]:
                        third -=1
                else: # if sum smaller
                    second += 1 # increase second without repitition
                    while second < third and nums[second] == nums[second - 1]:
                        second += 1
            first += 1
        return result

# TC - O(n * n)
# SC - O(n)
