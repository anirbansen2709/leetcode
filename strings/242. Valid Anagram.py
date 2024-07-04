from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)

        for char in s:
            s_dict[char] += 1

        for char in t:
            if char not in s_dict or s_dict[char] == 0:
                return False
            else:
                s_dict[char] -= 1

        for char, count in s_dict.items():
            if count != 0:
                return False
        return True

# TC - O(len)
# SC - O(len)
