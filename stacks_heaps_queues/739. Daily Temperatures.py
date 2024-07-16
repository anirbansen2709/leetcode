class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        length = len(temperatures)
        answer = [0 for _ in range(length)]
        for idx in range(length - 1, - 1, - 1):
            while stack and temperatures[stack[-1]] <= temperatures[idx] :
                stack.pop()
            if stack:
                answer[idx] = stack[-1] - idx
            stack.append(idx)
        return answer
