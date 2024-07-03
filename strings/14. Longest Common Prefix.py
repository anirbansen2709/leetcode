class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min([len(text) for text in strs])
        length = len(strs)
        prefix = ""
        
        for idx in range(min_len):
            char = strs[0][idx]
            for text_idx in range(1, length):
                if strs[text_idx][idx] != char:
                    return prefix
            prefix += char

        return prefix

# TC - O(n * m)
# SC - O(1)
