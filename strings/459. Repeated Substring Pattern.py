class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        for idx in range(1, length):
            if length % idx == 0:
                ideal_string = s[:idx] * (length // idx)
                if ideal_string == s:
                    return True
        return False

# TC - O(n)
# SC - O(1)
