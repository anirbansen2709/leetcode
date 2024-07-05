class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        char_set = set()
        max_len = 0
        left = 0
        right = 0

        while right < len(s):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right]) 
            max_len = max(max_len, right - left + 1)
            right += 1
        
        return max_len
            
# TC - O(n)
# SC - O(1)
