class Solution:
    def get_subsets(self, idx, path, answer):
        if idx == self.len:
            answer.append(list(path))
            return
        self.get_subsets(idx + 1, path, answer)
        self.get_subsets(idx + 1, path + [self.nums[idx]], answer)
        return

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.len = len(nums)
        answer = []
        self.get_subsets(0, [], answer)
        return answer

#TC - O(2^n)
#SC - O(n)
