class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        for idx in range(length - 1, -1, -1):
            if digits[idx] != 9:
                digits[idx] += 1
                return digits
            else:
                digits[idx] = 0
        return [1] + digits
      
# TC - O(n)
# SC - O(1)
