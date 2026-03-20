# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. 
# You may return the combinations in any order. The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the
# chosen numbers is different. The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# Recursive Backtracking
# 1. Base Cases (When to stop) - At the start of every recursive call, the code checks if it should stop exploring the current path:
# Success (target == 0): If the target has been perfectly reduced to zero, it means the numbers currently in your path add up exactly 
# to the original target. It appends this valid path to the answer list and returns.
# Out of Bounds (idx == len(candidates)): If you've looked through all the candidates and haven't hit a target of 0, this path is a dead 
# end. It returns to backtrack.
# 2. The "Don't Take" Decision
# self.get_sum(idx + 1, path, answer, candidates, target)
# The code decides to skip the current candidate entirely. It moves on to the next number in the list by incrementing idx to idx + 1.
# The path and the target remain unchanged.
# 3. The "Take" Decision
# if target >= val: First, it checks if the current candidate (val) is less than or equal to the remaining target. If it's larger, 
# taking it would result in a negative target, so it skips this step.
# self.get_sum(idx, path + [val], answer, candidates, target - val)
# If valid, it adds the current candidate to the path and subtracts its value from the target.
# Crucial detail: Notice that it passes idx without adding 1. Because the problem allows you to use the same number an unlimited number 
# of times, it stays on the same candidate so it can potentially choose it again in the next recursive step.
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

# TC - O(k * 2 ^ t) where k = avg length 
# SC - O(k * x)
