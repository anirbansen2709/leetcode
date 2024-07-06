class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answer = []
        for idx, interval in enumerate(intervals):
            if interval[0] > newInterval[1]:
                answer.append(newInterval)
                return answer + intervals[idx:]
            elif interval[1] < newInterval[0]:
                answer.append(interval)
            else:
                newInterval = [
                    min(newInterval[0], interval[0]),
                    max(newInterval[1], interval[1])
                ]
        answer.append(newInterval)
        return answer

# TC - O(n)
# SC - O(1)
