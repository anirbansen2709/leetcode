from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_dict = defaultdict(int)
        for char in s:
            char_dict[char] += 1
        total = 0
        for char, count in char_dict.items():
            if count > 1:
                total += (count//2) * 2
                count -= (count//2) * 2
            if total % 2 == 0 and count == 1:
                total += 1
        return total

# TC - O(n)
# SC - O(1)
