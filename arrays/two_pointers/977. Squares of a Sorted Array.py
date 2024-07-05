from collections import deque
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        answer = deque()
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                answer.appendleft(nums[left] ** 2)
                left += 1
            else:
                answer.appendleft(nums[right] ** 2)
                right -=1 
        return answer

# TC - O(n)
# SC - O(1)
