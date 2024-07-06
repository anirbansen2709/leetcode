class Solution:
    def get_all_comb(self, idx, ob, cb, path, answer):
        if idx == 2 * self.n:
            answer.append(str(path))
            return
        if ob > 0:
            self.get_all_comb(idx + 1, ob - 1, cb, path + '(', answer)
        if cb > 0 and cb > ob:
            self.get_all_comb(idx + 1, ob, cb - 1, path + ')', answer)
        return

    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        self.n = n
        self.get_all_comb(0, n, n, "", answer)
        return answer


# TC - O(2^n)
# SC - O(n)
