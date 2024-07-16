class Solution:
    def get_longest_length(self, text1, text2, p1, p2, dp):
        if p1 < 0 or p2 < 0:
            return 0
        if dp[p1][p2] != float('inf'):
            return dp[p1][p2]
        if text1[p1] == text2[p2]:
            dp[p1][p2] = 1 + self.get_longest_length(text1, text2, p1 - 1, p2 - 1, dp)
        else:
            remove1 = self.get_longest_length(text1, text2, p1 - 1, p2, dp)
            remove2 = self.get_longest_length(text1, text2, p1, p2 - 1, dp)
            dp[p1][p2] = max(remove1, remove2)
        return dp[p1][p2]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)
        dp = [[float('inf') for _ in range(len2 + 1)] for _ in range(len1 + 1)]
        return self.get_longest_length(text1, text2, len1 - 1, len2 - 1, dp)
