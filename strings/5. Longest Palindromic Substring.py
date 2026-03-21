# Given a string s, return the longest palindromic substring (A substring is a contiguous non-empty sequence of characters within a string.) in s.

# 1. The Strategy in longestPalindrome
# The Iteration: The for idx in range(len(s)): loop is the anchor. It systematically tests every index idx to see if it's the center of
# the longest palindrome.
# The "Odd" vs. "Even" Logic: Palindromes can have a single middle character (like "aba") or a double middle character (like "abba").
# odd = self.get_max_length(s, idx, idx) tests for an odd-length palindrome by starting the expansion with both pointers pointing to
# the exact same character (idx).
# even = self.get_max_length(s, idx, idx + 1) tests for an even-length palindrome by starting the expansion with pointers on the
# current character (idx) and the one immediately next to it (idx + 1).
# The Filter: The if/else block simply checks which of the two attempts (odd or even) yielded a longer string, storing the winner in 
# pal. If pal beats the running champion (max_pal), it takes the crown.
# 2. The Expansion Logic in get_max_length
# This is where the actual validation happens. Given a starting left and right center point, it tries to grow the palindrome outwards 
# layer by layer.
# The Boundaries: The while loop (while left >= 0 and right < len(s) ...) is the core logic engine. It ensures the pointers haven't 
# expanded beyond the start or end of the string.
# The Match Check: The final condition in the while loop (... and s[left] == s[right]) checks if the outer "shell" of characters matches. 
# If they don't, the palindrome ends, and the loop breaks.
# The Capture and Expand: If the characters match: It updates max_len = s[left:right+1] to save the newly validated palindrome.
# It pushes the pointers further out (left -= 1 to go left, right += 1 to go right) to check the next layer in the next loop iteration.

class Solution:
    def get_max_length(self, s, left, right):
        max_len = ""
        while left>= 0 and right < len(s) and s[left] == s[right]:
            max_len = s[left:right+1]
            left -= 1
            right += 1
        return max_len

    def longestPalindrome(self, s: str) -> str:
        max_pal = ""
        for idx in range(len(s)):
            odd = self.get_max_length(s, idx, idx)
            even = self.get_max_length(s, idx, idx + 1)
            if len(odd) > len(even):
                pal = odd
            else:
                pal = even
            if len(pal) > len(max_pal):
                max_pal = pal
        return max_pal

# TC - O(n * n)
# SC - O(1)
