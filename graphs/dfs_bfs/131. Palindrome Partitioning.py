class Solution:
    def is_palindrome(self, left, right):
        while left < right:
            if self.s[left] != self.s[right]:
                return False
            left += 1
            right -= 1
        return True

    def get_min_cut(self, idx, path, answer):
        if idx >= self.length:
            answer.append(list(path))
            return
        for end in range(idx, self.length):
            if self.is_palindrome(idx, end):
                path.append(self.s[idx:end + 1])
                self.get_min_cut(end + 1, path, answer)
                path.pop()
        return

    def partition(self, s: str) -> List[List[str]]:
        self.s = s
        self.length = len(s)
        answer = []
        self.get_min_cut(0, [], answer)
        return answer

# TC - O(2 ^ n * n/2 * k)
# SC - O(k)
