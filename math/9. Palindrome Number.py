class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        numbers = []
        while x:
            last_digit = x % 10
            x = x // 10
            numbers.append(last_digit)
        
        return numbers == numbers[::-1]

# TC - O(# of digits in x)
# SC - O(# of digits in x)
