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
