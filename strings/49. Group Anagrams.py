from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_dict = defaultdict(list)
        for text in strs:
            char_counts = [0 for _ in range(26)]
            for char in text:
                idx = ord(char) - ord('a')
                char_counts[idx] += 1
            char_dict[tuple(char_counts)].append(text)
        return char_dict.values()


# TC - O(n * m)
# SC - O(n * m)
