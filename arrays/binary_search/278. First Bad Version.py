# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0 
        high = n
        answer = -1
        while low <= high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        return answer

# TC - O(logn)
# SC - O(1)
