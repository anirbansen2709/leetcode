class Solution:
    def get_subsets(self, start, path, answer):
        answer.append(list(path))
        prev = -11
        for idx in range(start, self.length):
            num = self.nums[idx]
            if prev == num:
                continue
            self.get_subsets(idx + 1, path + [num], answer)
            prev = num
        return

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.nums = nums
        self.length = len(nums)
        answer = []
        self.get_subsets(0, [], answer)
        return answer

#TC - O(2^n)
#SC - O(n)
