# Given a string s, return the number of palindromic substrings in it. A string is a palindrome when it reads the same backward as forward. A substring is a contiguous sequence of characters
# within the string.

# Logic 
# It initializes a total count variable to 0. It loops through every character in the string s using its index idx. Inside the loop, it
# accounts for the two possible types of palindromes:
# Odd-length palindromes: These have a single character as the center. The code checks for these by calling self.get_counts(s, idx, idx).
# Even-length palindromes: These have a pair of identical characters as the center. The code checks for these by calling 
# self.get_counts(s, idx, idx + 1).
# It adds the results of both calls to the total count and returns it at the end.
# This function counts how many valid palindromes can be formed by expanding outwards from the given left and right indices.
# It initializes a local count to 0. It enters a while loop that continues to execute as long as three conditions are met:
# left >= 0: The left pointer hasn't gone past the start of the string. right < len(s): The right pointer hasn't gone past the end of 
# the string. s[left] == s[right]: The characters at the left and right pointers match (meaning it's still a valid palindrome).
# If all conditions are met, it means a palindrome was found. It increments the local count by 1.
# It then expands the window by moving the left pointer one step to the left (left -= 1) and the right pointer one step to the right 
# (right += 1).
# Once the loop breaks (because it hit an edge or the characters no longer match), it returns the count of palindromes found from that
# specific center.

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

# TC - O(n * n)
# SC - O(1)
