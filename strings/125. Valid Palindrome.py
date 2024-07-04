class Solution:

    def is_alnum(self, char):
        if (ord('a') <= ord(char) <= ord('z')) or (ord('A') <= ord(char) <= ord('Z')) or (ord('0') <= ord(char) <= ord('9')):
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and not self.is_alnum(s[left]):
                left += 1
            while left < right and not self.is_alnum(s[right]):
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1

        return True

# TC - O(n)
# SC - O(1)
