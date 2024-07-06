class Solution:
    def get_all_combs(self, start, path, answer, target):
        if target == 0:
            answer.append(list(path))
            return
        prev = -1
        for idx in range(start, self.length):
            num = self.candidates[idx]
            if prev == num:
                continue
            if target >= num:
                self.get_all_combs(idx + 1, path + [num], answer, target - num)
                prev = num
        return

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.candidates = candidates
        self.length = len(candidates)
        answer = []
        self.get_all_combs(0, [], answer, target)
        return answer

# TC - O(2^n)
# SC - O(n)
