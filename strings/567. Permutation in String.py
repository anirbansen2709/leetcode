from collections import defaultdict

class Solution:
    def is_same_dict(self, s1_dict, s2_dict):
        for key in s1_dict:
            if key not in s2_dict or s1_dict[key] != s2_dict[key]:
                return False
        return True  

    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False
        
        s1_dict = defaultdict(int)
        s2_dict = defaultdict(int)

        for idx in range(len_s1):
            s1_dict[s1[idx]] += 1
            s2_dict[s2[idx]] += 1

        if self.is_same_dict(s1_dict, s2_dict):
            return True

        for right in range(len_s1, len_s2):
            left = len_s1 - right
            s2_dict[s2[right]] += 1
            s2_dict[s2[left]] -= 1
            if self.is_same_dict(s1_dict, s2_dict):
                return True
        
        return False
