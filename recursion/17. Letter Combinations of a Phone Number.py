class Solution:
    def get_combinations(self, idx, answer, path):
        if idx == self.length:
            answer.append(str(path))
            return
        num = self.digits[idx]
        for char in self.mapping[int(num)]:
            print(path, char)
            self.get_combinations(idx + 1, answer, path + char)
        return

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.digits = digits
        self.length = len(digits)
        self.mapping = {
            2 : "abc",
            3 : "def",
            4 : "ghi",
            5 : "jkl",
            6 : "mno",
            7 : "pqrs",
            8 : "tuv",
            9 : "wxyz"
        }
        answer = []
        path = ""
        self.get_combinations(0, answer, path)
        return answer

# TC - O(4 ^ N)
# SC - O(4 ^ N)
