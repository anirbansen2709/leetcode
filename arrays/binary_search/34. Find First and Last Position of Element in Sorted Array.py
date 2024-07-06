class Solution:
    def find_first(self):
        left = 0
        right = self.length - 1
        answer = -1
        while left <= right:
            mid = (left + right) // 2
            if self.nums[mid] == self.target:
                answer = mid
                right = mid - 1
            elif self.nums[mid] > self.target:
                right = mid - 1
            else:
                left = mid + 1
        return answer
    
    def find_last(self):
        left = 0
        right = self.length - 1
        answer = -1
        while left <= right:
            mid = (left + right) // 2
            if self.nums[mid] == self.target:
                answer = mid
                left = mid + 1
            elif self.nums[mid] > self.target:
                right = mid - 1
            else:
                left = mid + 1
        return answer

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.length = len(nums)
        self.target = target
        first = self.find_first()
        if first != -1:
            last = self.find_last()
            return [first, last]
        else:
            return [-1, -1]

# TC - O(logn)
# SC - O(1)
