# Given a string s, find the length of the longest substring without duplicate characters. A substring is a contiguous non-empty sequence of characters within a string.

# Logic - 
# max_len: This integer variable stores the maximum length of a non-repeating substring encountered so far, initialized to 0.
# start: An integer pointer, initialized to 0, which marks the beginning of the current sliding window.
# last_seen: A dictionary that maps each character to its most recently seen index within the string.
# Window Expansion: The code iterates through the input string s using an end pointer, effectively expanding the right boundary of the 
# sliding window one character at a time. Character Examination: In each iteration, the character at s[end] (referred to as char) 
# is processed. Duplicate Handling: The algorithm checks if char is already present in the last_seen dictionary AND if its previously
# recorded index (last_seen[char]) is greater than or equal to the current start of the window. If both conditions are true, it 
# indicates that a repeating character has been found within the current non-repeating window. To resolve this, the start pointer is
# immediately moved to last_seen[char] + 1. This action effectively "jumps" the window's left boundary past the previous occurrence of
# the duplicate, ensuring the substring within the window remains unique.
# Update Last Seen Index: Regardless of whether a duplicate was found, the last_seen dictionary is updated to store the current end 
# index as the most recent position of char.
# Calculate and Update Max Length: The length of the current non-repeating substring is calculated as end−start+1. 
# The max_len variable is then updated to store the larger value between its current state and this newly calculated length.
# Return Final Result: After the end pointer has traversed the entire string, the max_len variable holds the final answer,
#representing the length of the longest substring without repeating characters.

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
