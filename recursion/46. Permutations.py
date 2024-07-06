class Solution:
    def get_all_perm(self, path, answer):
        if len(path) == len(self.nums):
            answer.append(list(path))
            return
        for idx in range(self.length):
            if self.nums[idx] not in path:
                path.append(self.nums[idx])
                self.get_all_perm(path, answer)
                path.pop()
        return

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.length = len(nums)
        answer = []
        self.get_all_perm([], answer)
        return answer

#TC - O(n! * n)
#SC - O(n)
