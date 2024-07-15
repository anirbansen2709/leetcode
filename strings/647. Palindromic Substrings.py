class Solution:
    def get_counts(self, s, left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count

    def countSubstrings(self, s: str) -> int:
        count = 0
        for idx in range(len(s)):
            count += self.get_counts(s, idx, idx)
            count += self.get_counts(s, idx, idx + 1)
        return count
