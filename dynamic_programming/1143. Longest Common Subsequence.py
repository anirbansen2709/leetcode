# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0. A subsequence of a string is a new string generated 
# from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters. For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

# Initialization (longestCommonSubsequence):You first store the lengths and the strings themselves as class attributes to avoid passing
# them continuously through recursive calls.You create a 2D array (dp) of size n * m (where n is the length of text1 and m is the length
# of text2), initialized with -1. This will store the longest common subsequence length for any given pair of indices.You kick off the 
# recursion starting at index 0 for both strings. Recursive Step (get_longest):Base Case: If either idx1 or idx2 reaches the end of its
# respective string, no more characters can be matched, so it returns 0.Memoization Check: If dp[idx1][idx2] is not -1, it means you've
# already solved this subproblem, so you return the stored result immediately.Match: If the current characters of both strings match 
# (self.text1[idx1] == self.text2[idx2]), they are part of the common subsequence. You add 1 and recursively check the rest of the 
# strings by advancing both indices.Mismatch: If the characters do not match, you branch into two possibilities:Skip the current 
# character in text1 (advance idx1).Skip the current character in text2 (advance idx2).You take the max() of these two choices, store
# it in your dp table to prevent future recalculations, and return it.

class Solution:
    def get_longest(self, idx1, idx2, dp):
        if idx1 == self.len1 or idx2 == self.len2:
            return 0
        if dp[idx1][idx2] != -1:
            return dp[idx1][idx2]
        if self.text1[idx1] == self.text2[idx2]:
            dp[idx1][idx2] = 1 + self.get_longest(idx1 + 1, idx2 + 1, dp)
            return dp[idx1][idx2]
        skip1 = self.get_longest(idx1 + 1, idx2, dp)
        skip2 = self.get_longest(idx1, idx2 + 1, dp)
        dp[idx1][idx2] = max(skip1, skip2)
        return dp[idx1][idx2]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.len1 = len(text1)
        self.len2 = len(text2)
        self.text1 = text1
        self.text2 = text2
        dp = [[-1 for _ in range(self.len2)] for _ in range(self.len1)]
        return self.get_longest(0, 0, dp)

# TC - O(n * m)
# SC - O(n * m)
