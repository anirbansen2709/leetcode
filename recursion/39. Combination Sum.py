class Solution:
    def get_sum(self, idx, path, answer, candidates, target):
        if target == 0:
            answer.append(path)
            return
        if idx == len(candidates):
            return
        #dont take
        self.get_sum(idx + 1, path, answer, candidates, target)
        # take
        val = candidates[idx]
        if target >= val:
            self.get_sum(idx, path + [val], answer, candidates, target - val)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        answer = []
        self.get_sum(0, path, answer, candidates, target)
        return answer

# TC - O(2 ^ t * k)
# SC - O(k * x)
