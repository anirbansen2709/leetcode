class Solution:
    def get_edit_distance(self, text1, text2, p1, p2, dp):
        if p1 < 0:
            return p2 + 1
        if p2 < 0:
            return p1 + 1
        if dp[p1][p2] != float('inf'):
            return dp[p1][p2]
        if text1[p1] == text2[p2]:
            dp[p1][p2] = self.get_edit_distance(text1, text2, p1 - 1, p2 - 1, dp)
        else:
            insert = self.get_edit_distance(text1, text2, p1 - 1, p2, dp)
            delete = self.get_edit_distance(text1, text2, p1, p2 - 1, dp)
            replace = self.get_edit_distance(text1, text2, p1 - 1, p2 - 1, dp)
            dp[p1][p2] = 1 + min(insert, delete, replace)
        return dp[p1][p2]

    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)
        dp = [[float('inf') for _ in range(len2 + 1)] for _ in range(len1 + 1)]
        return self.get_edit_distance(word1, word2, len1 - 1, len2 - 1, dp)

# TC - O(n * m)
# SC - O(n * m)
