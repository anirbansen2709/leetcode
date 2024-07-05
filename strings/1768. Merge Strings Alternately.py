class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        min_len = min(len1, len2)
        answer = ""
        for idx in range(min_len):
            answer += word1[idx]
            answer += word2[idx]
        if min_len != len1:
            answer += word1[idx+1:]
        if min_len != len2:
            answer += word2[idx+1:]
        return answer


# TC - O(max len1, len2)
# SC - O(1)
